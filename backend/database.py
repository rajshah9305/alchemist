# backend/database.py
import sqlite3
from typing import List, Dict, Any
import datetime
from contextlib import contextmanager
from .models import Interaction

DATABASE = "alchemist.db"

def init_db():
    try:
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS interactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    prompt TEXT NOT NULL,
                    response TEXT NOT NULL,
                    timestamp TEXT NOT NULL
                )
            ''')
            conn.commit()
    except sqlite3.Error as e:
        print(f"Database initialization error: {e}")

@contextmanager
def get_db():
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
        yield conn
    except sqlite3.Error as e:
        if conn:
            conn.rollback()
        raise e
    finally:
        if conn:
            conn.close()

def insert_interaction(interaction: Interaction) -> int:
    try:
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO interactions (prompt, response, timestamp) VALUES (?, ?, ?)",
                (interaction.prompt, interaction.response, interaction.timestamp)
            )
            conn.commit()
            return cursor.lastrowid
    except sqlite3.Error as e:
        print(f"Error inserting interaction: {e}")
        raise

def get_all_interactions() -> List[Dict[str, Any]]:
    try:
        with get_db() as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM interactions ORDER BY id DESC")
            rows = cursor.fetchall()
            return [dict(row) for row in rows]
    except sqlite3.Error as e:
        print(f"Error getting interactions: {e}")
        return []

def clear_interactions():
    try:
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM interactions")
            conn.commit()
            return cursor.rowcount
    except sqlite3.Error as e:
        print(f"Error clearing interactions: {e}")
        return 0
