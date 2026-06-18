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


def login_required(route):
    @wraps(route)
    def wrapper(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return route(*args, **kwargs)
    return wrapper



@app.route('/')
def index():
    return redirect(url_for('dashboard'))

@app.route('/insert/sample')
def run_insert_sample():
    db.insert_sample()
    return 'Database flushed and populated with some sample data.'

@app.route('/question/<int:question_id>')
def question_detail(question_id):

    con = db.get_db_con()

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

@app.route('/register', methods=['GET', 'POST'])
def register():
   return render_template('register.html')


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
        session['full_name'] =  user['first_name'] + ' ' + user['last_name']
        

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
    return render_template('leaderboard.html', users=[])

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')