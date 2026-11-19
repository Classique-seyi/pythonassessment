task_list = []

while True:
    print(f'''=====Menu choices=====:
1. add
2. view
3. remove
4. quit
======================
''')
    
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        task = input("Enter your task: ").strip()
        if task:
            task_list.append(task)
            print("Task added successfully")
        else:
            print("Task cannot be empty")
    elif choice == "2":
        if not task_list:
            print('''You have nothing in your to do list
Would you like to add something''')
        else:
            for index, task in enumerate(task_list, 1):
                print(index, task)
    elif choice == "3":
        if not task_list:
            print("Nothing to remove")
        else:
            try:
                task_number = int(input("Enter task to delete: "))
                index = task_number - 1 

                if 0 <= index < len(task_list):
                    task = task_list.pop(index)
                    print(f"Task {task_number} {task} removed successfully")
                else:
                    print("Task out of range")
            except ValueError:
                print("Please enter a valid number")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Input a valid number")