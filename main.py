import re
import json

global lst

def main():
    running = True
    while running:
        inp = input("add, display, modify, or close: ")
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
                running = False

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