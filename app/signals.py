from celery.signals import after_setup_task_logger, after_setup_logger,after_task_publish,task_prerun, task_postrun
from app import db
from app.models import Task
from datetime import datetime

''''@after_setup_task_logger.connect
def setup_loggers(logger, *args, **kwargs):

    sqlh = SQLAlchemyHandler()
    logger.addHandler(sqlh)

logger = logging.getLogger('celery')'''

@after_task_publish.connect
def task_sent_handler(sender=None, headers=None, body=None, **kwargs):
    print('fff')

    info = headers if 'task' in headers else body
    print(info)
    next_task = Task(task_id = info['id'],
                     task = info['task'],
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
                     published_at = datetime.now()
                    )
    db.session.add(next_task)
    db.session.commit()
    print('fjg')


@task_prerun.connect
def task_prerun_handler(sender=None, task_id=None,task=None,**kwargs):

    print('ggg')
    run_task = Task.query.filter_by(task_id = task_id).first()
    print(run_task['status'])
    run_task['status']='STARTED'
    db.session.add(run_task)
    db.session.commit()
    print('jj')@task_prerun.connect

@task_postrun.connect
def task_postrun_handler(sender=None, task_id=None,task=None,**kwargs):

    print('ggg')
    run_task = Task.query.filter_by(task_id = task_id).first()
    run_task['status']='Success'
    db.session.add(run_task)
    db.session.commit()
    print('jj')