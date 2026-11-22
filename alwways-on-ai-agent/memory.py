
import sqlite3

# Connect to database
db = sqlite3.connect("agent_memory.db")

# Create memory table
db.execute("""
CREATE TABLE IF NOT EXISTS memories (
    user_id TEXT,
    memory_key TEXT,
    memory_value TEXT,
    PRIMARY KEY(user_id, memory_key)
)
""")

# Save information
def remember(user_id, key, value):
    db.execute("""
    INSERT OR REPLACE INTO memories
    VALUES (?, ?, ?)
    """, (user_id, key, value))

    db.commit()
    print("Memory saved successfully!")


# Recall saved information
def recall(user_id):
    rows = db.execute("""
    SELECT memory_key, memory_value
    FROM memories
    WHERE user_id = ?
    """, (user_id,)).fetchall()

    return dict(rows)


# Save user preference
remember(
    "user-001",
    "preference",
    "Prefers Python-based AI projects"
)

# Read memory
print("\nAgent Memory:")
print(recall("user-001"))

