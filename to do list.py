def display_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Added task: {task}")

def remove_task(tasks):
    display_tasks(tasks)
    if tasks:
        try:
            task_number = int(input("Enter the task number to remove: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Removed task: {removed_task}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        print("\nTo-Do List Menu:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        
        choice = input("Choose an option (1/2/3/4): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Exiting the To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
