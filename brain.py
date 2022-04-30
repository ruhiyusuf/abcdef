from datetime import date, datetime
from hashlib import new
from os import ctermid
from tracemalloc import start
from turtle import update
from venv import create

class Task:
    # default values for status and startdate
    def __init__(self, name, status="Todo", startdate=datetime.now()): 
        self.name = name
        self.status = status
        self.startdate = startdate

# task list that will contain Task objects
task_list = [] 

# creates a Task object and appends to task_list
def create_task(task_name, task_status="Todo", task_startdate=datetime.now()):
    global task_list
    # create instance of class Task
    new_task = Task(task_name, task_status, task_startdate)
    task_list.append(new_task)
    print("created task", len(task_list))

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

# 3 columns/statuses to display
status_list = ["Todo", "Doing", "Done"] 

# return 3 lists with updated tasks under each status
def create_task_list_by_status():
    global task_list
    status_task_list = []
    # filter to store lists by status
    status_task_list.append(tasks_by_name(filter_by_status("Todo")))
    status_task_list.append(tasks_by_name(filter_by_status("Doing")))
    status_task_list.append(tasks_by_name(filter_by_status("Done")))

    return status_task_list

# displaying menu in table format in the command line
def show_menu():
    global task_list 
    task_list_displayed = [['', '', ''], status_list, ['', '', '']]
    task_list_displayed = transpose(create_task_list_by_status(), task_list_displayed)
    for row in task_list_displayed: 
        print("{: >20} {: >20} {: >20}".format(*row))

# return list of tasks with same status
def filter_by_status(filter_status):
    global task_list
    return list(filter(lambda x: x.status == filter_status, task_list))

# returns list of task names
def tasks_by_name(task_list):
    return list(map(lambda x: x.name, task_list))

# changes status of inputted task object
# to new inputted status
def change_status(task, updated_status):
    global task_list
    for i in task_list:
        if i == task:
            task.status = updated_status
            return
    return "cannot find task, please try again"

# returns Task object with inputted name
def find_task_by_name(task_name):
    global task_list
    for i in task_list:
        if i.name == task_name:
            return i
    return "cannot find task, please try again."

# adding default tasks
create_task("history project")
create_task("chem hw", task_status="Doing")
create_task("math hw", task_status="Doing")
create_task("csp test", task_status="Done")
create_task("finish essay", task_status="Done")
create_task("practice piano")

def run_app():
    global user_input, task_list, task_list_displayed 
    show_menu()
    print()
    print('showing menu...')

    # asks for user input
    user_input = input('')

    # while user has not wanted to quit/exit the program
    while not(user_input == 'q'):
        # change the status of a task
        if user_input == 'cs':
            task_name = input("Enter the name of the task: ")

            new_status = input("Enter the new status for this task: ")
            change_status(find_task_by_name(task_name), new_status)

            print(find_task_by_name(task_name).status)

            print("Your task status is now updated!")
        
        # create a new task
        if user_input.lower() == 'ct':
            task_name = input("Enter the name of the new task: ")

            task_status = input("Enter the status for this task: ")
            create_task(task_name, task_status)

            print("Your new task status has been created!")
        
        # show the board of tasks
        if user_input == 's':
            show_menu()
        
        # show help menu with commands
        if user_input == 'h':
            print("""
    ct      create task, are prompted for name and status
    cs      change status of task, prompted for task name and new status
    s       show board with tasks
    h       show help menu with commands
    q       quit/exit app
            """)
        
        # ask for user_input everytime while in the while loop
        user_input = input('').lower()

run_app()
