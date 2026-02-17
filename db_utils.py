import sqlite3
from datetime import datetime

def init_db():
    """Initializes the database and creates the history table."""
    conn = sqlite3.connect('chat_history.db')
    cursor = conn.cursor()
    # Using SQL to define the table structure
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS interactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            user_message TEXT,
            bot_response TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_to_db(user_input, bot_output):
    """Saves the conversation exchange to the database."""
    conn = sqlite3.connect('chat_history.db')
    cursor = conn.cursor()
    
    # Capture current time
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Standard SQL INSERT statement
    cursor.execute('''
        INSERT INTO interactions (timestamp, user_message, bot_response)
        VALUES (?, ?, ?)
    ''', (now, user_input, bot_output))
    
    conn.commit()
    conn.close()