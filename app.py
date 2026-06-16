import os
from flask import Flask, render_template, redirect, url_for, request, session
import db

app = Flask(__name__)

app.config.from_mapping(
    DATABASE=os.path.join(app.instance_path, 'studyswap.sqlite')
)
app.cli.add_command(db.init_db)
app.teardown_appcontext(db.close_db_con)

@app.route('/')
def index():
    return redirect(url_for('dashboard'))

@app.route('/insert/sample')
def run_insert_sample():
    db.insert_sample()
    return 'Database flushed and populated with some sample data.'

@app.route('/question/<int:question_id>')
def question_detail(question_id):
    return render_template('question_detail.html', question_id=question_id)

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
    return render_template('dashboard.html')