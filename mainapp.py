from backend import Task
from config import engine, session, sg


headers = ['ID', 'Task Name', 'Start Date', 'Finish Date', 'Status']
def update_table_data():
    tasks = session.query(Task).all()
    data = [[task.id, task.task_name, task.start_date, task.date_to_finish, task.status] for task in tasks]
    return data

tasks = session.query(Task).all()

data = [[task.id, task.task_name, task.start_date, task.date_to_finish, task.status] for task in tasks]

table = sg.Table(values=data,headings=headers, num_rows=10, key='-TABLE-' )

main_layout =[
[table],
[sg.Button('Exit')], [sg.Button('Delete Task')],
[sg.Button('Add Task')], [sg.Button('Edit Task')]
]

window = sg.Window('Tasks', main_layout)

while True:
    event, values = window.read()
    if event == 'Exit' or event == sg.WINDOW_CLOSED:
        break
    elif event == 'Delete Task':
        selected_row = values['-TABLE-']
        if selected_row:
            selected_task_id = selected_row[0]
            selected_task = session.query(Task).get(selected_task_id)
            if selected_task:
                session.delete(selected_task)
                session.commit()
                data = update_table_data()
                window['-TABLE-'].update(values=data)

window.close()