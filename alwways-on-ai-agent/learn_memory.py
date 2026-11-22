
import sqlite3

db = sqlite3.connect("agent_memory.db")

db.execute("""
CREATE TABLE IF NOT EXISTS memories (
    user_id TEXT,
    memory_key TEXT,
    memory_value TEXT,
    PRIMARY KEY(user_id, memory_key)
)
""")

# Take information from user
preference = input("What should I remember about you? ")

# Save information
db.execute("""
INSERT OR REPLACE INTO memories
VALUES (?, ?, ?)
""", ("user-001", "user_preference", preference))

db.commit()

# Recall information
result = db.execute("""
SELECT memory_value FROM memories
WHERE user_id = ? AND memory_key = ?
""", ("user-001", "user_preference")).fetchone()

print("\nYour AI Agent remembers:")
print(result[0])

db.close()
