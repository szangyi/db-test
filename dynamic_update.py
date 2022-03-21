import sqlite3

db = sqlite3.connect("database.sqlite")

user_id = "1"
user_name = "alex"
user_email = "a@a.com"

new_item = {"user_id":user_id}
set_parts = []

if user_name:
  set_parts.append("user_name=:user_name")
  new_item["user_name"] = user_name

if user_email:
  set_parts.append("user_email=:user_email")
  new_item["user_email"] = user_email

set_parts = ",".join(set_parts)

# INSERT, UPDATE, DELETE you must commit

db.execute(f"""
  UPDATE users
  SET {set_parts} 
  WHERE user_id = :user_id
""", new_item)

# Save the changes to the db
db.commit()

users = db.execute("SELECT * FROM users").fetchall()
print(users)

