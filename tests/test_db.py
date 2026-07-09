from db import get_connection


def test_get_connection_creates_table(tmp_db):
    conn = get_connection()
    cursor = conn.execute("PRAGMA table_info(history)")
    columns = [row[1] for row in cursor.fetchall()]
    assert "id" in columns
    assert "input_text" in columns
    assert "generated_text" in columns
    assert "date" in columns
    conn.close()


def test_insert_and_query(tmp_db):
    conn = get_connection()
    conn.execute(
        "INSERT INTO history (input_text, generated_text, date) VALUES (?, ?, ?)",
        ("test", "output", "2024-01-01"),
    )
    conn.commit()

    cursor = conn.execute("SELECT COUNT(*) FROM history")
    assert cursor.fetchone()[0] == 1
    conn.close()


def test_migrate_renames_model_column(tmp_db):
    import sqlite3

    conn = sqlite3.connect(tmp_db)
    conn.execute("""
        CREATE TABLE history
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
         input_text TEXT,
         model TEXT,
         date TEXT)
    """)
    conn.execute(
        "INSERT INTO history (input_text, model, date) VALUES (?, ?, ?)",
        ("old", "old output", "2023-01-01"),
    )
    conn.commit()
    conn.close()

    conn = get_connection()
    cursor = conn.execute("PRAGMA table_info(history)")
    columns = [row[1] for row in cursor.fetchall()]
    assert "generated_text" in columns
    assert "model" not in columns

    cursor = conn.execute("SELECT generated_text FROM history")
    assert cursor.fetchone()[0] == "old output"
    conn.close()
