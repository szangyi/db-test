import pymysql
import uuid
import json

# user = {
#     "user_id" : user_id,
#     "user_first_name" : user_first_name,
# }

newId = '5'
newName = 'Mari'

try:   
    db = pymysql.connect(host="localhost", port=8889,user="root",password="root", database="twitter")
    cur = db.cursor() #cursorClass in PyMyPy by default generates Dictionary as output
    sql = """INSERT INTO users (user_id, user_first_name) VALUES (%s, %s)"""
    val = (newId, newName)
    cur.execute(sql, val)
    db.commit()
except Exception as ex:
    print(type(ex))
finally:
    db.close()

# sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"


# user_id = str(uuid.uuid4())
# user_first_name = "helloanothername"
# user_email = "myother@email.com"

# user = {
#     "user_id" : user_id,
#     "user_first_name" : user_first_name,
#     "user_email" : user_email
# }

# try:

#     connection = pymysql.connect(host="localhost", user="root", passwd="", database="twitter")
#     cursor = connection.cursor()

#     insert1 = "INSERT INTO Artists(NAME, TRACK) VALUES('Towang', 'Jazz' );"

#     cursor.execute(insert1)

#     connection.commit()
# except Exception as ex:
#     print(type(ex))
#     if "user_email" in str(ex):
#         print("Email already exists")
# finally:
#     connection.close()