tasks = [
    {"description": "Wash Dishes", "completed": False, "time_taken": 10},
    {"description": "Clean Windows", "completed": False, "time_taken": 15},
    {"description": "Make Dinner", "completed": True, "time_taken": 30},
    {"description": "Feed Cat", "completed": False, "time_taken": 5},
    {"description": "Walk Dog", "completed": True, "time_taken": 60},
]


#
# access the tasks list
# check completed == true
# if false print a list of tasks
# if true print a list of completed tasks
#
#


# 1. Print a list of uncompleted tasks
def todo():
    for task in tasks:
        if task['completed'] == True:
            print(task)


todo()

# 2. Print a list of completed tasks


def done():
    for task in tasks:
        if task['completed'] == False:
            print(task)


done()


def notdone():
    for task in tasks:
        if task['completed'] == True:
            print('done', task)
        else:
            print('not done', task)


notdone()


# 3. Print a list of all task descriptions
def task_descriptions():
    for task in tasks:
        print(task['description'])


task_descriptions()


# 4. Print a list of tasks where time_taken is at least a given time
def find_me_a_task(time_available):
    # if task time is < time available, then print task
    for task in tasks:
        if task['time_taken'] <= time_available:
            print(task['description'])


find_me_a_task(20)

#
#  5. Print any task with a given description
# parameter is the description, print matching task


def task_details(task_description):
    for task in tasks:
        if task['description'] == task_description:
            print(task)


task_details('Walk Dog')


# 6. Given a description update that task to mark it as complete.

def task_done(task_description):
    for task in tasks:
        if task['description'] == task_description:
            # update the completed to TRUE
            task['completed'] = True
            # check it worked
            print(task)


task_done('Feed Cat')


# 7. Add a task to the list

def add_task(my_description, my_time_taken):
    tasks.append({"description": my_description,
                  "completed": False, "time_taken": my_time_taken})
    print(tasks[-1])


add_task('go home', 45)
