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
        selected_row = values['-TABLE-'] [0]
        to_delete = session.query(Task).filter_by(id = selected_row)
        if to_delete:
            session.delete
            session.commit

session.close()
window.close()

        # selected_task = values['-TABLE-'] [0] # Assuming 'Tasks' is the key for the table element in your GUI
        # task_to_delete = session.query(Task).filter_by(task_name=selected_task).first()
        # if task_to_delete:
        #     session.delete(task_to_delete)
        #     session.commit()
    # elif event == 'Delete Task':
    #     selected_rows = values['-TABLE-']  # Assuming 'Tasks' is the key for the table element in your GUI
    #     print(f'SELECTED ROWS: {selected_rows}')
    #     if len(selected_rows) != 1:
    #         sg.popup('Select one task to delete.')
    #     else:
    #         selected_task_id = int(selected_rows[0])
    #         print(f'SELECTED_TASK_ID: {selected_task_id}')
    #         selected_task = session.query(Task).get(selected_task_id)
    #         print(f'SELECTED_TASK: {selected_task}')
    #         confirm_msg = 'Are you sure you want to delete the selected task?'
    #         confirm_dialog = sg.popup_yes_no(confirm_msg, title='Confirm Deletion')
    #         if confirm_dialog == 'Yes':
    #             session.delete(selected_task)
    #             session.commit()
    #             sg.popup('Task(s) deleted successfully!')
                
