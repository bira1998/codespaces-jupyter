
from pathlib import Path
import sqlite3

# Create a note
def create_note(filename, content):

    folder = Path("agent_notes")
    folder.mkdir(exist_ok=True)

    safe_name = Path(filename).name
    path = folder / safe_name

    path.write_text(content, encoding="utf-8")

    return f"Note created: {path}"


# Save a task
def save_task(task, status="pending"):

    db = sqlite3.connect("agent_memory.db")

    db.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        task TEXT,
        status TEXT
    )
    """)

    db.execute(
        "INSERT INTO tasks VALUES (?, ?)",
        (task, status)
    )

    db.commit()
    db.close()

    return "Task saved successfully!"


# Tool registry
TOOLS = {
    "create_note": create_note,
    "save_task": save_task
}

print("Agent tools loaded successfully!")
