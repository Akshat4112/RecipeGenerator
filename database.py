from db import get_connection

if __name__ == "__main__":
    with get_connection() as conn:
        print("Database initialized successfully.")
        cursor = conn.execute("SELECT COUNT(*) FROM history")
        count = cursor.fetchone()[0]
        print(f"History table has {count} rows.")
