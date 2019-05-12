import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    ENGINE = 'db+mysql'
    USER = 'admin'
    PASSWORD = 'admin'
    HOST = '10.0.2.2'
    DATABASE = 'celery_control'

    def create_result_backend(engine,user,password,host,database):
        return '{engine}://{user}:{password}@{host}/{database}' \
            .format(engine=engine,user=user,password=password,host=host,database=database)

    SQLALCHEMY_DATABASE_URI = create_result_backend('mysql',USER,PASSWORD,HOST,DATABASE)

    CELERY_BROKER_URL='pyamqp://guest@localhost//',
    CELERY_RESULT_BACKEND=create_result_backend(ENGINE,USER,PASSWORD,HOST,DATABASE)
    CELERY_IMPORTS = ("app.tasks", )
    '''CELERY_QUEUES = (
        Queue('high', Exchange('high'), routing_key='high'),
        Queue('normal', Exchange('normal'), routing_key='normal'),
        Queue('low', Exchange('low'), routing_key='low'),
    )
    CELERY_DEFAULT_QUEUE = 'normal'
    CELERY_DEFAULT_EXCHANGE = 'normal'
    CELERY_DEFAULT_ROUTING_KEY = 'normal'''
    #CELERYD_HIJACK_ROOT_LOGGER = False