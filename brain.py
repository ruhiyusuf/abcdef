from datetime import date, datetime
from hashlib import new
from tracemalloc import start
from turtle import update
from venv import create

class Task:
    def __init__(self, name, status="Todo", startdate=datetime.now()):
        self.name = name
        self.status = status
        self.startdate = startdate

task_list = [] # its globallll 🌎

p1 = Task('abba')
p2 = Task('bccb')
task_list.append(p1)
task_list.append(p2)
# print(p1.name)

# x = [1]
# x.append(p1)
# x.append(Task(99))
# print("appened to list")
# print(x)
# del(x[-1])
# print(x[1].name)
# def create_task(): # pun intended 

def filter_by_status(filter_status):
    global task_list
    return list(filter(lambda x: x.status == filter_status, task_list))

def tasks_by_name():
    global task_list
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
        # break (?) should i break or nah, what if there is a duplicate, god help me

# def show_menu()

print(filter_by_status("Todo"))
print("task list", tasks_by_name())
create_task("New task")
print("last task date", task_list[-1].startdate)

# user_input = input('Enter your command: ')
# while not(user_input.lowercase() == 'q'):
