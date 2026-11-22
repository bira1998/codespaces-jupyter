
import sqlite3

db = sqlite3.connect("agent_memory.db")

rows = db.execute("""
SELECT memory_key, memory_value
FROM memories
WHERE user_id = ?
""", ("user-001",)).fetchall()

print("Previously Saved Memory:")
print(dict(rows))

db.close()
