import sqlite3
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_db_connection():
    """ Erstellt eine Verbindung zur SQLite-Datenbank """
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn

def create_user_table():
    """ Erstellt die User-Tabelle, falls sie nicht existiert """
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            hashed_password TEXT NOT NULL
        )
    """)
    cursor = conn.execute("SELECT username FROM users WHERE username = ?", ("neeco",))
    user_exists = cursor.fetchone()
    
    if not user_exists:
        # Testbenutzer erstellen
        hashed_password = pwd_context.hash("testuserpa$$")
        conn.execute(
            "INSERT INTO users (username, hashed_password) VALUES (?, ?)",
            ("neeco", hashed_password)
        )
    
    conn.commit()
    conn.close()

create_user_table()  
