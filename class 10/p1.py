import mysql.connector as mysql
con=mysql.connect(host="localhost", user="root", password="", db="newdb")
cur=con.cursor()
cur.execute("select * from student")
result=cur.fetchall()
for i in result:
    print(i)
con.commit()