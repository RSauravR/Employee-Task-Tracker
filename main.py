from db.database import Database
from models.task_manager import TaskManager

def main():
    db = Database("employee_tasks.db")
    task_manager = TaskManager(db)

    print("\nWelcome to the Employee Task Tracker!")
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()

    if not db.authenticate_user(username, password):
        print("Invalid credentials. Exiting...")
        return

    while True:
        print("\n--- Main Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task Status")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            task_manager.add_task(username)
        elif choice == "2":
            task_manager.view_tasks(username)
        elif choice == "3":
            task_manager.update_task(username)
        elif choice == "4":
            task_manager.delete_task(username)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
