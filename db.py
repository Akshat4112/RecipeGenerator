import sqlite3

from config import DATABASE_PATH


def _migrate_schema(conn: sqlite3.Connection) -> None:
    cursor = conn.execute("PRAGMA table_info(history)")
    columns = [row[1] for row in cursor.fetchall()]
    if "model" in columns and "generated_text" not in columns:
        conn.execute("ALTER TABLE history RENAME COLUMN model TO generated_text")
        conn.commit()


def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DATABASE_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS history
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
         input_text TEXT,
         generated_text TEXT,
         date TEXT)
    """)
    conn.commit()
    _migrate_schema(conn)
    return conn
