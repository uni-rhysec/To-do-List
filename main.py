import re
import json

global lst

def main(): 
    load()
    running=True
    while running:
        inp=input("add, display, modify, or close: ")
        match inp.lower():
            case "add":
                add()
                save()
            case "display":
                display()
            case "modify":
                modify()
                save()
            case "close":
                running=False

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

def save():
    string=json.dumps(lst)
    file=open("to do list.txt","w")
    file.write(string)
    file.close()

def add():
    
    name = input("Enter task name: ")
    while name.blank() or name.isspace():
        name = input("Enter task name: ")

    description = input("Enter task description: ")
    while description.blank() or description.isspace():
        description = input("Enter task name: ")
    
    date,success = get_date()
    while not success:
        date,success = get_date()

    task_dict = {"name":name,
                "desc.":description,
                "date due":date,
                "complete":False}
    lst.append(task_dict)

def load():
    global lst
    file=open("to do list.txt","r")
    string=file.read()
    file.close()
    lst=json.loads(string)