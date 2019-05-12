from app import celery
import app.signals



@celery.task
def add(x, y):
    return x + y


@celery.task
def mul(x, y):
    return x * y