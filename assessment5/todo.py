task_list = []

def add_task(task):
    task_list.append(task)
    return("Task added successfully")

def view_task(task):
    for index, task in enumerate(task_list, 1):
        print(index, task)

def remove_task(task_number):
    index = task_number - 1
    task = task_list.pop(index)
    print(f"{task} successfully deleted")

def main():
    while True:
        
        print(f'''=====Menu choices=====:
        1. add
        2. view
        3. remove
        4. quit
        ======================
        ''')

        choice = input("Enter your choice: ")
        if choice == "1":
            task = input(f"Add task: ")
        elif choice == "2":
            
            task = input(f"View task: ")
        elif choice == "3":
            task_number = int(input("Enter task number to remove: "))
        elif choice == "4":
            print("Quit")
            break
        else:
            print("Invalid task")
