import mysql.connector as mysql
con=mysql.connect(host="localhost", user="root", password="", db="newdb")
cur=con.cursor()
cur.execute("alter table student change stu_marks marks int")
