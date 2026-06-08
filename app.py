import os
from flask import Flask, render_template, redirect, url_for, request
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
    return f"Hier entsteht bald die Detailansicht fuer Frage-ID {question_id}"

@app.route('/register', methods=['GET', 'POST'])
def register():
   pass #muss erst noch implementiert werden


@app.route('/login', methods=['GET', 'POST'])
def login():
    pass #muss auch noch implementiert werden

@app.route('/question/create', methods=['GET', 'POST'])
def create_question():
    return "Hier entsteht bald das Formular zum Erstellen einer neuen Frage."

@app.route('/leaderboard')
def leaderboard():
    return "Hier entsteht bald das Leaderboard mit der Punkteuebersicht."

@app.route('/dashboard')
def dashboard():
    return "Hier entsteht bald das Dashboard mit den Fragen und Antworten."