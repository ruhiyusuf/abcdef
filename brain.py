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
status_list = ["Todo", "Doing", "Done"]

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
        # break (?) should i break or nah, what if there is a duplicate, god help me


print(filter_by_status("Done"))
print("task list", tasks_by_name(task_list))
create_task("New task")
print("last task date", task_list[-1].startdate)
create_task("doing this task", task_status="Doing")
create_task("doing 2", task_status="Doing")
create_task("im done!!", task_status="Done")
create_task("done 3", task_status="Done")
print(tasks_by_name(task_list))
def show_menu(status_task_list):
    global user_input
    # print("""
    # A) Create Task
    # B) Show Task
    # C) Change Task Details
    # """)
    # status_task_list = []
    # status_task_list.append(tasks_by_name(filter_by_status("Todo")))
    # status_task_list.append(tasks_by_name(filter_by_status("Doing")))
    # status_task_list.append(tasks_by_name(filter_by_status("Done")))
    # print('status task list')
    print(status_task_list)
    #max_list = max(map(lambda x: len(filter_by_status(status_list[i])), status_list))
    #for i in status_task_list:

    for row in status_task_list:
        print("{: >20} {: >20} {: >20}".format(*row))
       
            

    user_input = input('')

def create_the_list():
    status_task_list = []
    status_task_list.append(tasks_by_name(filter_by_status("Todo")))
    status_task_list.append(tasks_by_name(filter_by_status("Doing")))
    status_task_list.append(tasks_by_name(filter_by_status("Done")))

    max_list = max(map(lambda x: len(filter_by_status("Todo")), status_list))
    print("max list", max_list)

    new_list = [[],[]]
    
    for i in range(0, max_list):
        for j in range(0, 3):
            try:
                new_list[i].append(tasks_by_name(filter_by_status(status_list[j]))[i])
            except IndexError:
                pass
                #print(status_list[j])
                #new_list[i].append([])
                #new_list[i].append(tasks_by_name(filter_by_status(status_list[j]))[i])

                # if(tasks_by_name(filter_by_status(status_list[j]))[i]):
                #     new_list[i].append(tasks_by_name(filter_by_status(status_list[j]))[i])
                # else:
                #     new_list.append([[]])
                #new_list[i].append(tasks_by_name(filter_by_status(status_list[j]))[i])

    #new_list.append([])
    print('newlist')
    print(new_list)

    return new_list

create_the_list()
# show_menu()
# user_input = input('Enter your command: ')
# while not(user_input.lower() == 'q'):
#     show_menu()

show_menu(create_the_list())
