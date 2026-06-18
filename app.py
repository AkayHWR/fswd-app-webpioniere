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
    questions = con.execute(
        '''
        SELECT q.*, u.first_name || ' ' || u.last_name AS username
        FROM question q
        JOIN user u ON q.user_id = u.id
        ORDER BY q.id DESC
        '''
    ).fetchall()

    return render_template('dashboard.html', questions=questions)