import os

TASKS_FILE = 'tasks_data.txt'

def load_task_data():
    task_list = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            for line in file:
                task_id, details, due_date, status = line.strip().split(', ')
                task_list.append({
                    'id': int(task_id),
                    'details': details,
                    'due_date': due_date,
                    'status': status
                })
    return task_list

def save_task_data(task_list):
    with open(TASKS_FILE, 'w') as file:
        for task in task_list:
            file.write(f"{task['id']}, {task['details']}, {task['due_date']}, {task['status']}\n")

def create_task(task_list):
    details = input("Enter task details: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    task_id = len(task_list) + 1
    task_list.append({'id': task_id, 'details': details, 'due_date': due_date, 'status': 'Pending'})
    save_task_data(task_list)
    print("Task created successfully!")

def display_tasks(task_list):
    print("Task List:")
    pending_tasks = [task for task in task_list if task['status'] == 'Pending']
    completed_tasks = [task for task in task_list if task['status'] == 'Completed']

    if pending_tasks:
        print("[Pending Tasks]")
        for task in pending_tasks:
            print(f"{task['id']}. {task['details']} - Due: {task['due_date']}")
    else:
        print("[Pending Tasks] None available.")

    if completed_tasks:
        print("[Completed Tasks]")
        for task in completed_tasks:
            print(f"{task['id']}. {task['details']} - Due: {task['due_date']}")
    else:
        print("[Completed Tasks] None yet.")

def update_task(task_list):
    display_tasks(task_list)
    task_id = int(input("Enter the task number to update: "))
    for task in task_list:
        if task['id'] == task_id:
            new_details = input("Enter updated details: ")
            new_due_date = input("Enter updated due date (YYYY-MM-DD): ")
            task['details'] = new_details
            task['due_date'] = new_due_date
            save_task_data(task_list)
            print("Task updated successfully!")
            return
    print("Task not found.")

def remove_task(task_list):
    display_tasks(task_list)
    task_id = int(input("Enter the task number to delete: "))
    for task in task_list:
        if task['id'] == task_id:
            task_list.remove(task)
            save_task_data(task_list)
            print("Task removed successfully!")
            return
    print("Task not found.")

def complete_task(task_list):
    display_tasks(task_list)
    task_id = int(input("Enter the task number to mark as completed: "))
    for task in task_list:
        if task['id'] == task_id:
            task['status'] = 'Completed'
            save_task_data(task_list)
            print("Task marked as completed!")
            return
    print("Task not found.")

def todo_manager():
    task_list = load_task_data()
    while True:
        print("\nWelcome to Task Manager!")
        print("1. Add New Task")
        print("2. View All Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")
        user_choice = input("Select an option: ")

        if user_choice == '1':
            create_task(task_list)
        elif user_choice == '2':
            display_tasks(task_list)
        elif user_choice == '3':
            update_task(task_list)
        elif user_choice == '4':
            remove_task(task_list)
        elif user_choice == '5':
            complete_task(task_list)
        elif user_choice == '6':
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    todo_manager()
