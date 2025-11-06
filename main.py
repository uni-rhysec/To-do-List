import re
import json
import os

global lst

def main():
    load()
    running = True
    while running:
        inp = input("add, display, modify, complete, or close: ")
        match inp.lower():
            case "add":
                add()
                save()
            case "display":
                display()
            case "modify":
                modify()
                save()
            case "complete":
                complete()
                save()
            case "close":
                running = False
            case _:
                pass

def get_date():
    checking=True
    while checking:
        inp = input("Enter date in YYYY-MM-DD HH:MM format, or \"stop\" to cancel operation: ")
        if inp.lower() == "stop":
            return ("", False)
        if re.search("[0-9]{4}-[0-9]{2}-[0-9]{2} (0?[0-9]|1[0-9]|2[0-3]):([0-5][0-9])", inp):
            checking = False
            return (inp, True)
        print("Incorrect format!")

def save():
    string = json.dumps(lst)
    file = open("to do list.txt","w")
    file.write(string)
    file.close()

def load():
    global lst
    if not os.path.exists("to do list.txt"):
        lst = []
        return
    file = open("to do list.txt","r")
    string = file.read()
    file.close()
    lst = json.loads(string)

def select_task():
    display()
    checking = True
    while checking:
        inp = input("Select task using list number: ")
        if inp.isnumeric():
            if 0 < int(inp) and int(inp) <= len(lst):
                return int(inp) - 1
            else:
                print("No task with this number!")
        else:
            print("Invalid input")

def complete():
    global lst
    index=select_task()
    lst[index]["complete"]=True

def add():
    global lst
    name = input("Enter task name: ")
    desc = input("Enter task description: ")
    date_tuple = get_date()
    if not date_tuple[1]:
        print("Task addition cancelled")
        return
    date = date_tuple[0]
    complete = False
    lst.append({"name":name,"desc":desc,"date":date,"complete":complete})

def display():
    for i in range(len(lst)):
        task = lst[i]
        complete_str = "Not complete"
        if task["complete"]:
            complete_str = "Complete"
        string = f"{i+1}. {task["name"]}\n    {task["desc"]}\n    due: {task["date"]}\n    complete: {complete_str}"
        print(string)