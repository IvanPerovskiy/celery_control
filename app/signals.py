from celery.signals import after_task_publish, task_prerun, task_postrun, task_success, task_failure, task_retry
from app import db
from app.models import Task
from datetime import datetime


@after_task_publish.connect
def task_sent_handler(sender=None, headers=None, body=None, **kwargs):
    info = headers if 'task' in headers else body
    print(info)
    next_task = Task(task_id = info['id'],
                     task = info['task'],
                     args = info['argsrepr'],
                     kwargs = info['kwargsrepr'],
                     lang = info['lang'],
                     root_id = info['root_id'],
                     parent_id = info['parent_id'],
                     group = info['group'],
                     eta = str(info['eta']),
                     expires = str(info['expires']),
                     retries = info['retries'],
                     timelimit_soft = info['timelimit'][0],
                     timelimit_hard = info['timelimit'][1],
                     status = 'PENDING',
                     published_at = str(datetime.now())
                    )
    db.session.add(next_task)
    db.session.commit()


@task_prerun.connect
def task_prerun_handler(sender=None, task_id=None,task=None,**kwargs):
    run_task = Task.query.filter_by(task_id = task_id).first()
    run_task.status ='STARTED'
    run_task.begin = str(datetime.now())
    db.session.add(run_task)
    db.session.commit()


@task_success.connect
def task_success_handler(result=None,sender=None, **kwargs):
    success_task = Task.query.filter_by(task_id = sender.request.id).first()
    success_task.status ='SUCCESS'
    success_task.result=result
    def calculate_duration(begin):
        begin = datetime.strptime(begin, '%Y-%m-%d %H:%M:%S.%f')
        end = datetime.now()
        return str(end - begin)
    success_task.duration = calculate_duration(success_task.begin)
    db.session.add(success_task)
    db.session.commit()


@task_failure.connect
def task_failure_handler(sender=None, task_id=None, exception=None,
        args=None, kwargs=None, traceback=None, einfo=None, **kargs):
    failure_task = Task.query.filter_by(task_id = task_id).first()
    failure_task.status = 'FAILURE'
    failure_task.result = einfo
    db.session.add(failure_task)
    db.session.commit()


@task_retry.connect
def task_failure_handler(sender=None,request=None,einfo=None, **kargs):
    retry_task = Task.query.filter_by(task_id = request.id).first()
    retry_task.status = 'RETRY'
    retry_task.result = einfo
    db.session.add(retry_task)
    db.session.commit()