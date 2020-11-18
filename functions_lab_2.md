# Functions Lab

**Lab Duration: 60 minutes**

### Learning Objectives
- Learn how to break down code into smaller chunks
- Learn how to use functions to encapsulate code
- Refactor the task list program to use functions

### Brief

Given the following list of dictionaries, use functions throughout to create a program to manage a task list.

```python
tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]
```

### MVP

As a user, to manage my task list I would like a program that allows me to:

1. Print a list of uncompleted tasks

2. Print a list of completed tasks

3. Print a list of all task descriptions

4. Print a list of tasks where time_taken is at least a given time

5. Print any task with a given description


### Extension

6. Given a description update that task to mark it as complete.

7. Add a task to the list

### Further Extensions

8. Use a while loop to display the following menu and allow the use to enter an option.

```python
print("Menu:")
print("1: Display All Tasks")
print("2: Display Uncompleted Tasks")
print("3: Display Completed Tasks")
print("4: Mark Task as Complete")
print("5: Get Tasks Which Take Longer Than a Given Time")
print("6: Find Task by Description")
print("7: Add a new Task to list")
print("M or m: Display this menu")
print("Q or q: Quit")
```

9. Call the appropriate function depending on the users choice.
