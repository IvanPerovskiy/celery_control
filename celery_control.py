from app import app, db

@app.shell_context_processor
def make_shell_context():
    return {'db': db,'add':app.tasks.add,'Task':app.models.Task}