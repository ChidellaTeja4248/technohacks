tasks = []

def addtask(task):
    tasks.append(task)
    print(f"Added task:{task}")


# deleting the task in the list if exist
def delete_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"removed task is {task}")
    else:
        print(f"{task}  not found")


# To see what are the task in the Todolist
def viewtask():
    print(" my todo list: ")
    for i, task in enumerate(tasks):
        print(f"{i + 1}.{task}")


while True:
    print("\n what operation u want to do")
    print("1. add the task")
    print("2. delete the task")
    print("3. view the task")
    print("4. exit ")

    choice = input(" enter the choice u want to do")
    if choice == "1":
        task = input("add the new task:")
        addtask(task)
    elif choice == "2":
        task = input("enter the task to delete:")
        delete_task(task)
    elif choice == "3":
        viewtask()
    elif choice == "4":
        print("existing tasks are these:")
        break
    else:
        print("invalid choice you have made ")
