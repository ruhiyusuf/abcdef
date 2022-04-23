from datetime import date, datetime
from hashlib import new
from os import ctermid
from tracemalloc import start
from turtle import update
from venv import create

class Task:
    def __init__(self, name, status="Todo", startdate=datetime.now()):
        self.name = name
        self.status = status
        self.startdate = startdate

task_list = [] # its globallll 🌎

status_list = ["Todo", "Doing", "Done"] 

def transpose(srcList, destList): 
  # convert variable length list to 2D list of same length
  m = max(map(lambda srcList: len(srcList), srcList))
  for i in range(0, len(srcList)):
    while len(srcList[i]) < m:
      srcList[i].append('')

  for i in range(0, len(srcList[0])):
    row = []
    for item in srcList: 
      row.append(item[i])
    destList.append(row)
    
  return destList

def filter_by_status(filter_status):
    global task_list
    return list(filter(lambda x: x.status == filter_status, task_list))

def tasks_by_name(task_list):
    return list(map(lambda x: x.name, task_list))

def create_task(task_name, task_status="Todo", task_startdate=datetime.now()): # pun intended
    global task_list
    new_task = Task(task_name, task_status, task_startdate)
    task_list.append(new_task)
    print("created task", len(task_list))

def change_status(task, updated_status):
    global task_list
    for i in task_list:
        if i == task:
            task.status = updated_status
            return
        else:
            continue
    return "cannot find task, please try again"

def find_task_by_name(task_name):
    global task_list
    for i in task_list:
        if i.name == task_name:
            return i
    return "cannot find task, please try again."

def create_task_list_by_status():
    global task_list
    status_task_list = []
    status_task_list.append(tasks_by_name(filter_by_status("Todo")))
    status_task_list.append(tasks_by_name(filter_by_status("Doing")))
    status_task_list.append(tasks_by_name(filter_by_status("Done")))

    return status_task_list

create_task("history project")
create_task("chem hw", task_status="Doing")
create_task("math hw", task_status="Doing")
create_task("csp test", task_status="Done")
create_task("finish essay", task_status="Done")
create_task("practice piano")

def show_menu():
    global task_list 
    task_list_displayed = [['', '', ''], status_list, ['', '', '']]
    task_list_displayed = transpose(create_task_list_by_status(), task_list_displayed)
    for row in task_list_displayed: 
        print("{: >20} {: >20} {: >20}".format(*row))

def run_app():
    global user_input, task_list, task_list_displayed 
    show_menu()
    print()
    print('showing menu...')

    user_input = input('')
    while not(user_input == 'q'):
        if user_input == 'cs':
            task_name = input("Enter the name of the task: ")

            new_status = input("Enter the new status for this task: ")
            change_status(find_task_by_name(task_name), new_status)

            print(find_task_by_name(task_name).status)

            print("Your task status is now updated!")
        if user_input.lower() == 'ct':
            task_name = input("Enter the name of the new task: ")

            task_status = input("Enter the status for this task: ")
            create_task(task_name, task_status)

            print("Your new task status has been created!")
        if user_input == 's':
            show_menu()
        if user_input == 'h':
            print("""
    ct      create task, are prompted for name and status
    cs      change status of task, prompted for task name and new status
    s       show board with tasks
    h       show help menu with commands
    q       quit/exit app
            """)
        user_input = input('').lower()

run_app()
