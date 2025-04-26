class TaskManager:
    def __init__(self, db):
        self.db = db

    def add_task(self, username):
        task = input("Enter task description: ").strip()
        deadline = input("Enter deadline (YYYY-MM-DD): ").strip()

        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (username, task, deadline) VALUES (?, ?, ?)", (username, task, deadline))
        conn.commit()
        conn.close()
        print("✅ Task added successfully!")

    def view_tasks(self, username):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, task, status, deadline FROM tasks WHERE username=?", (username,))
        tasks = cursor.fetchall()
        conn.close()

        if not tasks:
            print("No tasks found.")
            return

        print("\nYour Tasks:")
        for task in tasks:
            print(f"ID: {task[0]}, Task: {task[1]}, Status: {task[2]}, Deadline: {task[3]}")

    def update_task(self, username):
        self.view_tasks(username)
        task_id = input("Enter the Task ID to update: ").strip()
        new_status = input("Enter new status (Pending/Completed/Overdue): ").strip()

        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET status=? WHERE id=? AND username=?", (new_status, task_id, username))
        conn.commit()
        conn.close()
        print("✅ Task updated successfully!")

    def delete_task(self, username):
        self.view_tasks(username)
        task_id = input("Enter the Task ID to delete: ").strip()

        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id=? AND username=?", (task_id, username))
        conn.commit()
        conn.close()
        print("✅ Task deleted successfully!")
