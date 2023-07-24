# Lists containing the items on your to-do list
art_ToDo = []
art_Complete = ["clean brushes", "change water"]
programming_ToDo = []
programming_Complete = []
school_ToDo = []
school_Complete = []

# Dictionary combining all the items on you to do list
taskList = {"Art (To Do)": art_ToDo,
            "Art (Completed)": art_Complete,
            "Programming (To Do)": programming_ToDo,
            "Programming (Completed)": programming_Complete,
            "School (To Do)": school_ToDo,
            "School (Completed)": school_Complete
            }

# possible categories
categories = ["Art (To Do)", "Programming (To Do)", "School (To Do)"]
mark_complete_categories = ["Art", "Programming", "School"]


# possible actions
def possible_actions():
    print("Adding a Task: 1")
    print("Mark Task as Complete: 2")
    print("Print List: 3")


# Initial display
print(" ")
print("To Do List")
print(taskList)
print(" ")
possible_actions()
action = input("Action (1, 2, 3):  ")

# Adding a task
while action == "1":
    print(" ")
    user_task = str(input("Task Name: "))
    user_category = input("Task Category: ")
    print(" ")
    # checks for valid category
    if user_category not in categories:
        print("Please enter a valid category [Art (To Do), Programming (To Do), School (To Do)]")
        user_category = input("Task Category: ")
        # checks if task has already been added
        if user_task in taskList[user_category]:
            print("This task has already been added")
            print(" ")
            possible_actions()
            action = input("Action (1, 2, 3):  ")
        else:
            if user_category == "Art (To Do)":
                art_ToDo.append(user_task)
                print(taskList)
                print(" ")
                possible_actions()
                action = input("Action (1, 2, 3):  ")
            elif user_category == "Programming (To Do)":
                programming_ToDo.append(user_task)
                print(taskList)
                print(" ")
                possible_actions()
                action = input("Action (1, 2, 3):  ")
            elif user_category == "School (To Do)":
                school_ToDo.append(user_task)
                print(taskList)
                print(" ")
                possible_actions()
                action = input("Action (1, 2, 3):  ")
    else:
        # adds task to appropriate category
        if user_category == "Art (To Do)":
            if user_task in art_ToDo:
                print()
                print("This task has already been added")
                print()
                possible_actions()
                action = input("Action (1, 2, 3):  ")
            else:
                print()
                art_ToDo.append(user_task)
                print(taskList)
                print(" ")
                possible_actions()
                action = input("Action (1, 2, 3):  ")
        elif user_category == "Programming (To Do)":
            if user_task in programming_ToDo:
                print()
                print("This task has already been added")
                print()
                possible_actions()
                action = input("Action (1, 2, 3):  ")
            else:
                programming_ToDo.append(user_task)
                print(taskList)
                print(" ")
                possible_actions()
                action = input("Action (1, 2, 3):  ")
        elif user_category == "School (To Do)":
            if user_task in school_ToDo:
                print()
                print("This task has already been added")
                print()
                possible_actions()
                action = input("Action (1, 2, 3):  ")
            else:
                school_ToDo.append(user_task)
                print(taskList)
                print(" ")
                possible_actions()
                action = input("Action (1, 2, 3):  ")


# function that marks task as complete
def mark_complete(task, category):
    if category == "Art":
        art_ToDo.remove(task)
        art_Complete.append(task)
    elif category == "Programming":
        programming_ToDo.remove(task)
        programming_Complete.append(task)
    elif category == "Programming":
        school_ToDo.remove(task)
        school_Complete.append(task)
    return taskList


# marks tasks as complete
while action == "2":
    print()
    complete_task = input("Complete Task Name: ")
    complete_category = input("Complete Task Category (Art, Programming, School): ")
    print()
    # checks if category is valid
    while complete_category not in mark_complete_categories:
        print("Please Enter a Valid Category (Art, Programming, School")
        complete_category = input("Complete Task Category: ")
    # checks if task has already been complete
    if complete_task in art_Complete or programming_Complete or school_Complete:
        print("You Have Already Completed This Task")
        print(" ")
        possible_actions()
        action = input("Action (1, 2, 3):  ")
    # checks if task is on the to do list
    elif complete_task not in art_ToDo or programming_ToDo or school_ToDo:
        print("Please Enter a Task on Your To-Do List")
        complete_task = input("Complete Task Name: ")
    # marks the task as complete
    while complete_task in art_ToDo or programming_ToDo or school_ToDo and complete_category in mark_complete_categories:
        print(mark_complete(complete_task, complete_category))
        print(" ")
        possible_actions()
        action = input("Action (1, 2, 3):  ")

# prints to do list
while action == "3":
    print(" ")
    print("To-Do List")
    print(" ")
    for key in taskList:
        print(key, ":", taskList[key])
    print()
    print(" ")
    print("Adding a Task: 1")
    print("Mark Task as Complete: 2")
    print("Print List: 3")
    action = input("Action (1, 2, 3):  ")
