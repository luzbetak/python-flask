#!/usr/bin/env python3.8

from flask import Flask, request
from flask import render_template
from flask import redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    done = db.Column(db.Boolean, default=False)

    def __init__(self, content):
        self.content = content
        self.done = False

    def __repr__(self):
        return '<Content %s>' % self.content


db.create_all()


@app.route('/')
def listTasks():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)


@app.route('/task', methods=['POST'])
def addTask():
    content = request.form['content']
    if not content:
        return 'Error'

    task = Task(content)
    db.session.add(task)
    db.session.commit()
    return redirect('/todo')


@app.route('/delete/<int:task_id>')
def delTask(task_id):
    task = Task.query.get(task_id)
    if not task:
        return redirect('/todo')

    db.session.delete(task)
    db.session.commit()
    return redirect('/todo')


@app.route('/done/<int:task_id>')
def resolveTask(task_id):
    task = Task.query.get(task_id)

    if not task:
        return redirect('/todo')
    if task.done:
        task.done = False
    else:
        task.done = True

    db.session.commit()
    return redirect('/todo')


if __name__ == '__main__':
    app.run()
