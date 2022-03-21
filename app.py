import pymysql
import uuid
import json


try:   
    db = pymysql.connect(host="localhost", port=8889,user="root",password="root", database="twitter", cursorclass=pymysql.cursors.DictCursor)
    cur = db.cursor() #cursorClass in PyMyPy by default generates Dictionary as output
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    print(users)
except Exception as ex:
    print(type(ex))
finally:
    db.close()







# BUFFEEEEER
# return dictionary at gets
# if else at return (if logged in that redirect here otherwise there)
# show tweets id, time all those at the tweets page as %tweet in tweets {{tweet[0]}}

# ADD USER
# separate values and sql command
# sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
# val = ('webmaster@python.org', 'very-secret')
# cur.execute(sql,val )
