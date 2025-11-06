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
        inp=input("Enter date in YYYY-MM-DD HH:MM format, or \"stop\" to cancel operation: ")
        if inp.lower()=="stop":
            return ("",False)
        if re.search("[0-9]{4}-[0-9]{2}-[0-9]{2} (0?[0-9]|1[0-9]|2[0-3]):([0-5][0-9])", inp):
            checking=False
            return (inp,True)
        print("Incorrect format!")

def select_operation():
    print("Select an operation (1-5).\n" \
            "1. Edit name\n" \
            "2. Edit description\n" \
            "3. Edit date\n" \
            "4. Toggle completed\n" \
            "5. Delete task")
    valid = False
    while not valid:
        try:
            choice = int(input("Select a number: "))
            if choice > 0 and choice <= 5:
                valid = True
            else:
                print("Invalid task number.")
        except:
            print("Invalid task number.")
    return choice


def modify():
    global lst
    #lst = [{"name": "task1", "desc": "task1 desc","date":"2025-11-06 10:00","complete":True}, {"name": "task2", "date": "2090-11-06 09:26"}] # example
    input = select_task() # 
    task_to_edit = lst[input]
    operation = select_operation()
    match operation:
        case 1:
            new_name = ("Enter new name: ")
            task_to_edit.update({"name": new_name})
        case 2:
            new_desc = ("Enter new description: ")
            task_to_edit.update({"desc": new_desc})
        case 3:
            new_date = get_date()
            task_to_edit.update({"date": new_date})
        case 4:
            if task_to_edit.get("complete"):
                task_to_edit.update({"complete": False})
            else:
                task_to_edit.update({"complete": True})
        case 5:
            lst.pop(input)

def save():
    string = json.dumps(lst)
    file = open("to do list.txt","w")
    file.write(string)
    file.close()

def add():
    global lst

    name = input("Enter task name: ")
    while name.blank() or name.isspace():
        name = input("Enter task name: ")

    description = input("Enter task description: ")
    while description.blank() or description.isspace():
        description = input("Enter task description: ")
    
    date,success = get_date()
    if not success:
        print("Task addition cancelled")
        return

    task_dict = {"name":name,
                "desc":description,
                "date":date,
                "complete":False}
    lst.append(task_dict)

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

def display():
    for i in range(len(lst)):
        task = lst[i]
        complete_str = "Not complete"
        if task["complete"]:
            complete_str = "Complete"
        string = f"{i+1}. {task["name"]}\n    {task["desc"]}\n    due: {task["date"]}\n    complete: {complete_str}"
        print(string)
