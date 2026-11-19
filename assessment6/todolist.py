tasks = []

while True:
    print('''Menu:
1. add
2. view
3. remove
4. done
5. quit
''')

    choice = input().strip()

    if choice == "1":
        task = input("Enter task: ")
        if task:
            tasks.append([task, 0])
            print("Task added successfully!")
        else:
            print("Task cannot be empty")
    elif choice == "2":
        if not tasks:
            print("Nothing to view")
        else:
            for index, task in enumerate(tasks, 1):
                i = index - 1
                print(f"[ ] {index}. {tasks[i][0]}" if tasks[i][1] == 0 else f"[x] {index}. {tasks[i][0]}")

    elif choice == "3":
        if not tasks:
            print("Nothing to remove")
        else:
            try:
                task_number = int(input("Enter task number to delete: "))
                index = task_number - 1

                if 0 <= index < len(tasks):
                    tasks.pop(index)
                    print("Task removed successfully!")
                else:
                    print("Task out of range")
            except ValueError:
                print("Enter a valid task number")

    elif choice == "4":
        if not tasks:
            print("Nothing to complete")
        else:
            try:
                task_number = int(input("Enter task number to complete: "))
                index = task_number - 1
                print(tasks)

                if 0 <= index < len(tasks):
                    print(f'Task {task_number} marked as done.')
                    tasks[index][1] = 1
                    print(tasks)
                else:
                    print("Task out of range")
            except ValueError:
                print("Enter a valid task number")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Enter a number from 1-5")


