import os
import re
from functools import wraps
from flask import Flask, render_template, redirect, url_for, request, session
import db

app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY = 'secret_key_just_for_dev_environment',
    DATABASE=os.path.join(app.instance_path, 'studyswap.sqlite')
)
app.cli.add_command(db.init_db)
app.teardown_appcontext(db.close_db_con)


def hashtags_from_text(text):
    tags = re.findall(r'#[A-Za-z0-9_ÄÖÜäöüß]+', text)
    return sorted(set(tags))

def all_hashtags():
    con = db.get_db_con()
    rows = con.execute('SELECT hashtags FROM question').fetchall()
    counts = {}
    for row in rows:
        for tag in hashtags_from_text(row['hashtags']):
            counts[tag] = counts.get(tag, 0) + 1
    return sorted(counts.items(), key=lambda item: item[1], reverse=True)

def login_required(route):
    @wraps(route)
    def wrapper(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return route(*args, **kwargs)
    return wrapper




def calculate_points(user_id):
    con = db.get_db_con()
    upvotes = con.execute(
        'SELECT COUNT(*) FROM answer_vote WHERE vote = 1 AND answer_id IN (SELECT id FROM answer WHERE user_id = ?)',
        (user_id,)
    ).fetchone()[0]
    downvotes = con.execute(
        'SELECT COUNT(*) FROM answer_vote WHERE vote = -1 AND answer_id IN (SELECT id FROM answer WHERE user_id = ?)',
        (user_id,)
    ).fetchone()[0]
    solutions = con.execute(
        'SELECT COUNT(*) FROM answer WHERE user_id = ? AND is_solution = 1',
        (user_id,)
    ).fetchone()[0]
    return upvotes - downvotes + solutions * 5







@app.route('/')
def index():
    return redirect(url_for('dashboard'))

@app.route('/insert/sample')
def run_insert_sample():
    db.insert_sample()
    return 'Database flushed and populated with some sample data.'

@app.route('/question/<int:question_id>', methods=['GET', 'POST'])
def question_detail(question_id):

    con = db.get_db_con()

    if request.method == 'POST':

        content = request.form['content'].strip()

        con.execute(
            '''
            INSERT INTO answer(question_id, user_id, content)
            VALUES (?, ?, ?)
            ''',
            (
                question_id,
                session['user_id'],
                content
            )
        )

        con.commit()

        return redirect(
            url_for(
                'question_detail',
                question_id=question_id
            )
        )

    question = con.execute(
        '''
        SELECT q.*, u.first_name || ' ' || u.last_name AS username
        FROM question q
        JOIN user u ON q.user_id = u.id
        WHERE q.id = ?
        ''',
        (question_id,)
    ).fetchone()

    if question is None:
        return redirect(url_for('dashboard'))

    answers = con.execute(
        '''
        SELECT a.*, u.first_name || ' ' || u.last_name AS username
        FROM answer a
        JOIN user u ON a.user_id = u.id
        WHERE a.question_id = ?
        ORDER BY a.id DESC
        ''',
        (question_id,)
    ).fetchall()

    return render_template(
        'question_detail.html',
        question=question,
        answers=answers
    )

def hwr_email(email):
    email = email.strip().lower()
    return email.endswith('@stud.hwr-berlin.de')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        if 'user_id' in session:
            return redirect(url_for('dashboard'))

        return render_template('register.html')
    else:  # POST request method
        first_name = request.form['first_name'].strip()
        last_name = request.form['last_name'].strip()
        email = request.form['email'].strip().lower()
        password = request.form['password'].strip()
        confirm_password = request.form['confirm_password'].strip()

        if not first_name or not last_name or not email or not password:
            return render_template(
                'register.html',
                error='Bitte fülle alle Felder aus.'
            )

        if not hwr_email(email):
            return render_template(
                'register.html',
                error='Bitte verwende deine HWR-E-Mail-Adresse.'
            )

        if password != confirm_password:
            return render_template(
                'register.html',
                error='Die Passwörter stimmen nicht überein.'
            )

        con = db.get_db_con()

        existing_user = con.execute(
            'SELECT * FROM user WHERE email = ?',
            (email,)
        ).fetchone()

        if existing_user is not None:
            return render_template(
                'register.html',
                error='Für diese E-Mail-Adresse existiert bereits ein Account.'
            )

        cursor = con.execute(
            '''
            INSERT INTO user (email, first_name, last_name, password)
            VALUES (?, ?, ?, ?)
            ''',
            (email, first_name, last_name, password)
        )
        con.commit()

        session.clear()
        session['user_id'] = cursor.lastrowid
        session['username'] = first_name + ' ' + last_name

        return redirect(url_for('dashboard'))



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'user_id' in session:
            return redirect(url_for('dashboard'))

        return render_template('login.html')

    else:  # POST request method
        email = request.form['email'].strip()
        password = request.form['password'].strip()

        con = db.get_db_con()
        user = con.execute(
            'SELECT * FROM user WHERE email = ?',
            (email,)
        ).fetchone()

        if user is None or user['password'] != password:
            return render_template(
                'login.html',
                error='E-Mail oder Passwort ist falsch.'
            )

        session.clear()
        session['user_id'] = user['id']
        session['username'] =  user['first_name'] + ' ' + user['last_name']
        

        return redirect(url_for('dashboard'))
    

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('dashboard'))


@app.route('/question/create', methods=['GET', 'POST'])
@login_required
def create_question():
    if request.method == 'POST':
        title = request.form['title'].strip()
        description = request.form['description'].strip()
        hashtags = ' '.join(hashtags_from_text(request.form['hashtags']))

        if title == '' or description == '':
            return render_template('create_question.html', error='Titel und Beschreibung sind Pflicht.')
        if hashtags == '':
            return render_template('create_question.html', error='Bitte trage mindestens einen Hashtag ein.')

        con = db.get_db_con()
        con.execute(
            'INSERT INTO question (user_id, title, description, hashtags) VALUES (?, ?, ?, ?)',
            (session['user_id'], title, description, hashtags)
        )
        con.commit()
        return redirect(url_for('dashboard'))

    return render_template('create_question.html')



@app.route('/leaderboard')
def leaderboard():
    con = db.get_db_con()
    users = con.execute("SELECT id, first_name || ' ' || last_name AS username FROM user").fetchall()
    leaderboard_users = []

    for user in users:
        answer_count = con.execute(
            'SELECT COUNT(*) FROM answer WHERE user_id = ?',
            (user['id'],)
        ).fetchone()[0]
        solution_count = con.execute(
            'SELECT COUNT(*) FROM answer WHERE user_id = ? AND is_solution = 1',
            (user['id'],)
        ).fetchone()[0]
        leaderboard_users.append({
            'username': user['username'],
            'points': calculate_points(user['id']),
            'answer_count': answer_count,
            'solution_count': solution_count
        })

    leaderboard_users.sort(key=lambda user: user['points'], reverse=True)
    return render_template('leaderboard.html', users=leaderboard_users)

@app.route('/dashboard')
def dashboard():
    con = db.get_db_con()
    search = request.args.get('q', '').strip()
    selected_tags = request.args.getlist('tag')


    questions = con.execute(
        '''
        SELECT q.*, u.first_name || ' ' || u.last_name AS username, COUNT(a.id) AS answer_count
        FROM question q
        JOIN user u ON q.user_id = u.id
        LEFT JOIN answer a ON a.question_id = q.id
        WHERE q.title LIKE ? OR q.description LIKE ?
        GROUP BY q.id
        ORDER BY q.id DESC
        ''',
        (f'%{search}%', f'%{search}%')
    ).fetchall()

    if selected_tags:
        questions = [
            question for question in questions
            if all(tag in hashtags_from_text(question['hashtags']) for tag in selected_tags)
        ]

    tags = all_hashtags()
    top_tags = tags[:5]
    other_tags = tags[5:]

    return render_template(
        'dashboard.html', 
        questions=questions,
        search=search,
        selected_tags=selected_tags,
        top_tags=top_tags,
        other_tags=other_tags
    )