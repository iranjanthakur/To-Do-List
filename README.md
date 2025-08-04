# To-Do List Manager 📝

A simple, console-based to-do list application built with Python for task management and productivity.

## 🎯 Project Overview

This project was developed as part of the **Python Developer Internship** assignment. It implements a persistent command-line interface (CLI) to-do list manager that allows users to efficiently manage their daily tasks.

## ✨ Features

- **Add Tasks**: Create new tasks with descriptions and timestamps
- **View Tasks**: Display all tasks with completion status and creation dates
- **Remove Tasks**: Delete specific tasks by their number
- **Toggle Completion**: Mark tasks as completed or pending
- **Clear Completed**: Remove all completed tasks at once
- **Persistent Storage**: Tasks are automatically saved to and loaded from a file
- **User-Friendly Interface**: Clean, menu-driven console experience
- **Error Handling**: Robust input validation and file handling

## 🛠️ Technical Implementation

### Core Technologies
- **Python 3.x**
- **JSON** for data serialization
- **File I/O** for persistent storage
- **Object-Oriented Programming** principles

### Key Concepts Demonstrated
- **File Handling**: Reading from and writing to files using `open()`
- **Lists**: Dynamic task storage and manipulation
- **String Manipulation**: Input validation and formatting
- **Error Handling**: Try-catch blocks for robust operation
- **Data Structures**: Dictionaries for structured task objects

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher installed on your system

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/todo-list-manager.git
   cd todo-list-manager
   ```

2. Run the application:
   ```bash
   python todo.py
   ```

### Usage
1. Launch the application
2. Choose from the menu options (1-6):
   - **1**: Add a new task
   - **2**: View all tasks
   - **3**: Remove a task
   - **4**: Mark task as complete/pending
   - **5**: Clear all completed tasks
   - **6**: Save and exit

## 📁 File Structure

```
todo-list-manager/
│
├── todo.py           # Main application file
├── tasks.txt         # Data storage file (auto-generated)
├── README.md         # Project documentation
└── screenshots/      # Application screenshots (optional)
```

## 💾 Data Storage

Tasks are stored in JSON format in `tasks.txt` with the following structure:
```json
[
  {
    "id": 1,
    "description": "Complete Python assignment",
    "completed": false,
    "created_at": "2024-08-04 10:30:00"
  }
]
```

## 🔧 Code Structure

### Classes
- **`TodoManager`**: Main class handling all task operations
  - `load_tasks()`: Load tasks from file
  - `save_tasks()`: Save tasks to file
  - `add_task()`: Add new task
  - `view_tasks()`: Display all tasks
  - `remove_task()`: Remove specific task
  - `toggle_task_completion()`: Mark task complete/pending
  - `clear_completed_tasks()`: Remove completed tasks

### Functions
- **`display_menu()`**: Show main menu options
- **`get_user_choice()`**: Handle user input validation
- **`main()`**: Main program loop

## 📋 Interview Questions Addressed

1. **File I/O**: Uses `open()` with context managers and JSON serialization
2. **File Modes**: Implements 'r' for reading and 'w' for writing
3. **String Methods**: Uses `strip()` for input validation
4. **Lists**: Dynamic list operations with indexing and iteration
5. **List Methods**: Demonstrates `append()`, `pop()`, and list comprehensions
6. **Element Removal**: Multiple approaches including `pop()` and filtering
7. **Context Managers**: Proper file handling with `with` statements
8. **File Processing**: JSON parsing for structured data handling
9. **Data Structures**: Dictionary objects for complex task attributes
10. **File Existence**: `os.path.exists()` for safe file operations

## 🎨 Sample Output

```
========================================
TO-DO LIST MANAGER
========================================
1. Add Task
2. View Tasks
3. Remove Task
4. Mark Task Complete/Pending
5. Clear Completed Tasks
6. Save & Exit
========================================

==================================================
YOUR TO-DO LIST
==================================================
1. [○] Complete Python assignment
   Created: 2024-08-04 10:30:00
2. [✓] Review code documentation
   Created: 2024-08-04 09:15:00
==================================================
Total: 2 tasks | Completed: 1 | Pending: 1
```

## 🔍 Error Handling

The application includes comprehensive error handling for:
- Invalid user input
- File read/write operations
- JSON parsing errors
- Empty task descriptions
- Invalid task numbers

## 📝 License

This project is created for educational purposes as part of a Python Developer Internship program.

## 👨‍💻 Author

**Your Name**
- GitHub: [@Ranjan Thakur](https://github.com/iranjanthakur)
- Email: ranjanreignsthakur@gmail.com

## 🙏 Acknowledgments

- Python Developer Internship Program
- Python community for excellent documentation
- Stack Overflow for troubleshooting guidance

---

**Note**: This project demonstrates fundamental Python concepts including file handling, data structures, and user interface design in a console application.
