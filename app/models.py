from sqlalchemy import Column
from sqlalchemy.types import DateTime, Integer, String
from app  import db


class Task(db.Model):
    id = Column(Integer, primary_key=True) # auto incrementing
    task_id = Column(String(128))
    task = Column(String(32))
    args = Column(String(128))
    kwargs = Column(String(128))
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
    result = Column(String(1024))
    begin = Column(String(128))
    duration = Column(String(128))
    published_at = Column(DateTime)





