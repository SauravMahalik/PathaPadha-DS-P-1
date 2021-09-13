import mysql.connector as mysql
con=mysql.connect(host="localhost", user="root", password="", db="newdb")
cur=con.cursor()
cur.execute("show databases")
for i in cur:
    print(i)