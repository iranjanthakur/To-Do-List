import os
import json
from datetime import datetime

class TodoManager:
    def __init__(self, filename="tasks.txt"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from file if it exists"""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as file:
                    content = file.read().strip()
                    if content:
                        self.tasks = json.loads(content)
                    else:
                        self.tasks = []
            else:
                self.tasks = []
        except (json.JSONDecodeError, FileNotFoundError):
            print(f"Warning: Could not load tasks from {self.filename}. Starting with empty list.")
            self.tasks = []
    
    def save_tasks(self):
        """Save tasks to file"""
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.tasks, file, indent=2)
            print(f"Tasks saved to {self.filename}")
        except Exception as e:
            print(f"Error saving tasks: {e}")
    
    def add_task(self, description):
        """Add a new task to the list"""
        if not description.strip():
            print("Task description cannot be empty!")
            return
        
        task = {
            'id': len(self.tasks) + 1,
            'description': description.strip(),
            'completed': False,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        print(f"Task added: '{description}'")
    
    def view_tasks(self):
        """Display all tasks"""
        if not self.tasks:
            print("\nNo tasks found! Your to-do list is empty.")
            return
        
        print(f"\n{'='*50}")
        print("YOUR TO-DO LIST")
        print(f"{'='*50}")
        
        for i, task in enumerate(self.tasks, 1):
            status = "✓" if task['completed'] else "○"
            print(f"{i}. [{status}] {task['description']}")
            if 'created_at' in task:
                print(f"   Created: {task['created_at']}")
        
        print(f"{'='*50}")
        completed = sum(1 for task in self.tasks if task['completed'])
        print(f"Total: {len(self.tasks)} tasks | Completed: {completed} | Pending: {len(self.tasks) - completed}")
    
    def remove_task(self, task_number):
        """Remove a task by its number"""
        try:
            if 1 <= task_number <= len(self.tasks):
                removed_task = self.tasks.pop(task_number - 1)
                # Update IDs for remaining tasks
                for i, task in enumerate(self.tasks):
                    task['id'] = i + 1
                print(f"Task removed: '{removed_task['description']}'")
            else:
                print(f"Invalid task number! Please choose between 1 and {len(self.tasks)}")
        except (ValueError, IndexError):
            print("Invalid task number!")
    
    def toggle_task_completion(self, task_number):
        """Mark a task as completed or pending"""
        try:
            if 1 <= task_number <= len(self.tasks):
                task = self.tasks[task_number - 1]
                task['completed'] = not task['completed']
                status = "completed" if task['completed'] else "pending"
                print(f"Task marked as {status}: '{task['description']}'")
            else:
                print(f"Invalid task number! Please choose between 1 and {len(self.tasks)}")
        except (ValueError, IndexError):
            print("Invalid task number!")
    
    def clear_completed_tasks(self):
        """Remove all completed tasks"""
        initial_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if not task['completed']]
        # Update IDs
        for i, task in enumerate(self.tasks):
            task['id'] = i + 1
        
        removed_count = initial_count - len(self.tasks)
        if removed_count > 0:
            print(f"Removed {removed_count} completed task(s)")
        else:
            print("No completed tasks to remove")

def display_menu():
    """Display the main menu"""
    print(f"\n{'='*40}")
    print("TO-DO LIST MANAGER")
    print(f"{'='*40}")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Mark Task Complete/Pending")
    print("5. Clear Completed Tasks")
    print("6. Save & Exit")
    print(f"{'='*40}")

def get_user_choice():
    """Get and validate user input"""
    try:
        choice = int(input("Enter your choice (1-6): "))
        return choice
    except ValueError:
        return None

def main():
    """Main program loop"""
    print("Welcome to the To-Do List Manager!")
    todo_manager = TodoManager()
    
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == 1:
            # Add Task
            task_desc = input("\nEnter task description: ")
            todo_manager.add_task(task_desc)
        
        elif choice == 2:
            # View Tasks
            todo_manager.view_tasks()
        
        elif choice == 3:
            # Remove Task
            todo_manager.view_tasks()
            if todo_manager.tasks:
                try:
                    task_num = int(input("\nEnter task number to remove: "))
                    todo_manager.remove_task(task_num)
                except ValueError:
                    print("Please enter a valid number!")
        
        elif choice == 4:
            # Toggle Task Completion
            todo_manager.view_tasks()
            if todo_manager.tasks:
                try:
                    task_num = int(input("\nEnter task number to toggle completion: "))
                    todo_manager.toggle_task_completion(task_num)
                except ValueError:
                    print("Please enter a valid number!")
        
        elif choice == 5:
            # Clear Completed Tasks
            todo_manager.clear_completed_tasks()
        
        elif choice == 6:
            # Save & Exit
            todo_manager.save_tasks()
            print("Thank you for using To-Do List Manager! Goodbye!")
            break
        
        else:
            print("Invalid choice! Please select a number between 1 and 6.")
        
        # Pause before showing menu again
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
