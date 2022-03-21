import sqlite3
import uuid

user_id = str(uuid.uuid4())
# user_name = "helloanothername"

user = {
    "user_name" : "blaaaaae"
}

try:
    db = sqlite3.connect("database.sqlite")

    # using a dictionairy and named pacehollders
    counter = db.execute("DELETE FROM users WHERE user_name = :user_name", user).rowcount
    if not counter: print("nothing was deleted")

    # using questionmarks as placeholders
    # db.execute("DELETE FROM users WHERE user_name = ?", (user_name,))
    db.commit()
except Exception as ex:
    print(type(ex))
    if "user_name" in str(ex):
        print("There is no user like that")
finally:
    db.close()