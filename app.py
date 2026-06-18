import os
import re
from flask import Flask, render_template, redirect, url_for, request
import db

app = Flask(__name__)

app.config.from_mapping(
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
    return render_template('login.html')

@app.route('/question/create', methods=['GET', 'POST'])
def create_question():
    return render_template('create_question.html')

@app.route('/leaderboard')
def leaderboard():
    return render_template('leaderboard.html', users=[])

@app.route('/dashboard')
def dashboard():
    con = db.get_db_con()
    search = request.args.get('q', '').strip()
    selected_tags = request.args.getlist('tag')


    questions = con.execute(
        '''
        SELECT q.*, u.first_name || ' ' || u.last_name AS username
        FROM question q
        JOIN user u ON q.user_id = u.id
        WHERE q.title LIKE ? OR q.description LIKE ?
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

    return render_template(
        'dashboard.html', 
        questions=questions,
        search=search,
        selected_tags=selected_tags,
        tags=tags
    )