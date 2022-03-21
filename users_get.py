import sqlite3
import json

################################ make the array json
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

try:
    db = sqlite3.connect("database.sqlite")
    db.row_factory = dict_factory
    users = json.dumps(db.execute("SELECT * FROM users").fetchall())
    print(users)
except Exception as ex:
    print(type(ex))
finally:
    db.close()
