from datetime import date
from backend import Base, Task
from config import session, engine

Base.metadata.create_all(engine)

tasks = []
tasks.append(Task(task_name='Clean the house', start_date= '2023-05-11', date_to_finish= '2023-05-12', status= "Done" ))
tasks.append(Task(task_name='Prepare dinner', start_date= '2023-05-31', date_to_finish= '2023-06-12', status= "Will Start" ))
tasks.append(Task(task_name='Learn to code', start_date= '2023-05-11', date_to_finish= '2023-05-12', status= "Ongoing" ))
tasks.append(Task(task_name='Finish coding course', start_date= '2023-05-11', date_to_finish= '2023-07-19', status= "Ongoing" ))
session.add_all(tasks)

session.commit()
