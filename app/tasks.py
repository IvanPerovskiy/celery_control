from app import celery
import app.signals

@celery.task
def add(x, y):
    return x + y

@celery.task
def mul(x, y):
    return x * y

@celery.task
def mul(x, y):
    return x * y

@celery.task
def div(x, y):
    try:
        res = x/y
    except ZeroDivisionError:
       return False
    return res

@celery.task
def gen_numbers(x,y,z):
    result = [i for i in range(x) if i % y == 0 or i % z == 0]
    return result