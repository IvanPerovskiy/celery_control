from sqlalchemy import Column
from sqlalchemy.types import DateTime, Integer, String
from sqlalchemy.sql import func
from app  import db


class Task(db.Model):
    id = Column(Integer, primary_key=True) # auto incrementing
    task_id = Column(String(128))
    task = Column(String(32))
    lang = Column(String(32))
    root_id = Column(String(128))
    parent_id = Column(String(128))
    group = Column(String(128))
    eta = Column(String(128))
    expires = Column(String(128))
    retries = Column(Integer)
    timelimit_soft = Column(Integer)
    timelimit_hard = Column(Integer)
    status = Column(String(16))
    comment = Column(String(128)) # info, debug, or error?
    priority = Column(String(16))
    rules = Column(String(128))
    trace = Column(String(64)) # the full traceback printout
    msg = Column(String(64)) # any custom log you may have included
    run_at = Column(DateTime) # the current timestamp
    published_at = Column(DateTime)