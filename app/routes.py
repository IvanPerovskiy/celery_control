from app import app
from flask import render_template
from app.tasks import add,mul

@app.route('/')
@app.route('/index')
def index():
    add.apply_async((128,128),countdown = 10)
    add.apply_async((128,128),countdown = 100)
    mul.apply_async((128,128),countdown = 50)
    return render_template('index.html')


@app.route('/active')
def active():
    return render_template('active.html')

@app.route('/history')
def history():
    return render_template('history.html')