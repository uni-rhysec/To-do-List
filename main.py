def main():
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