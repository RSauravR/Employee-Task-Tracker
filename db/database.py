import sqlite3
import hashlib

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.create_tables()

    def create_tables(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                task TEXT,
                status TEXT DEFAULT 'Pending',
                deadline TEXT,
                FOREIGN KEY (username) REFERENCES users(username)
            )
        ''')

        conn.commit()
        conn.close()

    def authenticate_user(self, username, password):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        password_hash = hashlib.sha256(password.encode()).hexdigest()

        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password_hash))
        user = cursor.fetchone()

        if not user:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password_hash))
            conn.commit()
            conn.close()
            print("New user created successfully!")
            return True

        conn.close()
        return True

    def get_connection(self):
        return sqlite3.connect(self.db_name)
