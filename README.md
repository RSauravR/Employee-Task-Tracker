# Employee Task Tracker

A simple Python + SQLite-based CLI tool for managing employee tasks. This application allows employees to securely log in, add tasks, view tasks, update task statuses, and delete tasks. It uses an SQLite database to store user and task data.

## Features

- **User Authentication**: Secure login system with SHA256 password hashing.
- **Task Management**:
  - Add new tasks with descriptions and deadlines.
  - View existing tasks.
  - Update task status (Pending, Completed, or Overdue).
  - Delete tasks when completed.
- **Database Integration**: Automatically creates an SQLite database (`employee_tasks.db`) to store user credentials and tasks.
  
## Usage

1. **Run the script**:

   ```bash
   python main.py
