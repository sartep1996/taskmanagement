from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Task(Base):
    __tablename__ = "Tasks"
    id = Column(Integer, primary_key=True)
    task_name = Column('Task_name', String(50))
    start_date = Column('Start_date', String(50))
    date_to_finish = Column('Date_to_finish', String(50))
    status = Column('Status', String(50))

    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return self.task_name if self.task_name else ''