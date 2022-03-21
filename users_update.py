import sqlite3
import uuid

user_id = str(uuid.uuid4())

user = {
    "user_id" : "076c70b1-665b-4472-a56c-75f2829cfb20",
    "user_name" : "NEWNEWname"
}

try:
    db = sqlite3.connect("database.sqlite")

    # 3 keywords: UPDATE, SET, WHERE

    # using a dictionairy and named pacehollders
    counter = db.execute("""
        UPDATE users
        SET user_name = :user_name
        WHERE user_id = :user_id
    """, user).rowcount
    db.commit()
    print(counter)
except Exception as ex:
    print(type(ex))
finally:
    db.close()


# using questionmarks as placeholders
# counter = db.execute("""
#     UPDATE users
#     SET user_name = ? 
#     WHERE user_id = ?
# """, ("NEW USER NAME", "076c70b1-665b-4472-a56c-75f2829cfb20")).rowcount
# db.commit()
# print(counter)