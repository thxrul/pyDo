import sys
import json
from json import JSONDecodeError
from pathlib import Path

filename = Path("toDoList.json")
if not filename.is_file():
    filename.touch()


def newTask():
    thingToDo = input("Enter your task: \n")
    timeToDo = input("Enter time the activity is due: \n")
    taskDic = {
        "Task" : thingToDo,
        "Due" : timeToDo
    }
    taskList = []
    taskList.append(taskDic)
    with open("toDoList.json", "r+") as file:
        try:
            filedata = json.load(file)
        except JSONDecodeError:
            filedata = []
        filedata.extend(taskList)
        file.seek(0)
        file.truncate()
        json.dump(filedata, file, indent=4)
    

def listTasks():
    with open("toDoList.json", "r") as file:
        try:
            tasks = json.load(file)
        except JSONDecodeError:
            print("No tasks found.")
            return
        
        if not tasks:
            print("No tasks found.")
            return
        
        index = 1
        for task in tasks:
            print(f"{index}. {task['Task']} -- Due {task['Due']}")

def removeTask():
        with open("toDoList.json", "r+") as file:
            try:
                tasks = json.load(file)
            except JSONDecodeError:
                print("No tasks found.")
                return

            if not tasks:
                print("No tasks found.")
                return

            index = 1
            for task in tasks:
                print(f"{index}. {task['Task']} -- Due {task['Due']}")
                index += 1
            
            toRemove = int(input("Enter the number of the task you want to remove: ")) - 1

            if 0 <= toRemove < len(tasks):
                del tasks[toRemove]
                file.seek(0)
                file.truncate()
                json.dump(tasks, file, indent=4)
            else:
                print("Enter a valid number.")
                removeTask()

            return

def helpPage():
    print('Use "pydo help" to bring up this page.\n\n "pydo list"    Print out the list of tasks and their times.\n "pydo add"    Add a new task\n "pydo remove"    Remove a task\n')
    input("Enter any key to exit.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No user input. Please run "pydo help" to get a list of commands. ')
        sys.exit(1)

    usrArg = sys.argv[1].lower()

    if usrArg == "add" or usrArg == "new":
        newTask()
    elif usrArg == "list":
        listTasks()
    elif usrArg == "remove":
        removeTask()
    elif usrArg == "help":
        helpPage()
    else:
        print(f"Invalid command {usrArg}")