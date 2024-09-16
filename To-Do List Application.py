
tasks = []

def display_tasks():
    print("To-Do List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added!")

def update_task():
    display_tasks()
    task_number = int(input("Enter the task number to update: "))
    task = input("Enter the updated task: ")
    tasks[task_number - 1] = task
    print("Task updated!")

def delete_task():
    display_tasks()
    task_number = int(input("Enter the task number to delete: "))
    del tasks[task_number - 1]
    print("Task deleted!")

while True:
    print("\n1. Display Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Quit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        display_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
