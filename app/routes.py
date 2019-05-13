from app import app
from flask import render_template
from app.tasks import add, mul, gen_numbers, div
from app.models import Task
from datetime import datetime,timedelta

@app.route('/')
@app.route('/index')
def index():
    add.apply_async((128,128),countdown = 10)
    add.apply_async((128,128),countdown = 100)
    mul.apply_async((128,128),countdown = 50)
    gen_numbers.apply_async((100000000,7,17), eta =datetime.now() + timedelta(hours=2))
    gen_numbers.delay(1000000,13,23)
    div.delay(500,5)
    div.delay(500,0)
    return render_template('index.html')


@app.route('/active')
def active():
    active_tasks = Task.query.filter_by(status = 'STARTED').all()
    future_tasks = Task.query.filter_by(status = 'PENDING').all()
    retry_tasks = Task.query.filter_by(status = 'RETRY').all()
    return render_template('active.html',active_tasks=active_tasks,
                           future_tasks =future_tasks, retry_tasks=retry_tasks)

@app.route('/history')
def history():
    success_tasks = Task.query.filter_by(status='SUCCESS').all()
    failure_tasks = Task.query.filter_by(status='FAILURE').all()
    return render_template('history.html', success_tasks=success_tasks, failure_tasks=failure_tasks)