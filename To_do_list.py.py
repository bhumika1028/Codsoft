import json
import os

TODO_FILE = 'tasks.json'

def load_tasks():
    """Load tasks from the JSON file."""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(description, due_date=None):
    """Add a new task to the list."""
    tasks = load_tasks()
    tasks.append({"description": description, "due_date": due_date, "completed": False})
    save_tasks(tasks)
    print(f"Task added: '{description}'")

def list_tasks():
    """List all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        due_date = task.get("due_date", "N/A")
        print(f"{i}. {task['description']} (Due: {due_date}) [{status}]")

def update_task(task_id, description=None, due_date=None, completed=None):
    """Update an existing task."""
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        if description:
            tasks[task_id]["description"] = description
        if due_date:
            tasks[task_id]["due_date"] = due_date
        if completed is not None:
            tasks[task_id]["completed"] = completed
        save_tasks(tasks)
        print(f"Task {task_id + 1} updated.")
    else:
        print(f"Task {task_id + 1} not found.")

def delete_task(task_id):
    """Delete a task."""
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        removed_task = tasks.pop(task_id)
        save_tasks(tasks)
        print(f"Task '{removed_task['description']}' deleted.")
    else:
        print(f"Task {task_id + 1} not found.")

def mark_task_completed(task_id):
    """Mark a task as completed."""
    update_task(task_id, completed=True)

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")
        
        if choice == '1':
            description = input("Enter task description: ")
            due_date = input("Enter due date (optional, YYYY-MM-DD): ")
            add_task(description, due_date)
        
        elif choice == '2':
            list_tasks()
        
        elif choice == '3':
            list_tasks()
            task_id = int(input("Enter the task number to update: ")) - 1
            description = input("Enter new description (leave blank to keep current): ")
            due_date = input("Enter new due date (leave blank to keep current): ")
            update_task(task_id, description or None, due_date or None)
        
        elif choice == '4':
            list_tasks()
            task_id = int(input("Enter the task number to delete: ")) - 1
            delete_task(task_id)
        
        elif choice == '5':
            list_tasks()
            task_id = int(input("Enter the task number to mark as completed: ")) - 1
            mark_task_completed(task_id)
        
        elif choice == '6':
            print("Exiting application.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
