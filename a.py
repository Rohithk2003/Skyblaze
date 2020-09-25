import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="rohithk123")
mycursor=mydb.cursor()
mycursor.execute("use classxiia1")
mycursor.execute("set autocommit=1")
print('1.Insert n records into the table Emp')
print('2.Display details of the table emp')
choice = int(input("enter your choice"))
if choice == 1:
	n = int(input("enter no of records"))
	for i in range(n):
		empno = int(input("enter employee number"))
		name = input("enter name of the employee")
		gender = input("enter the gender of the employee")
		salary = int(input("enter salary of the employee"))
		dept = input("enter deptname")
		mycursor.execute('insert into Emp values(%s,%s,%s,%s,%s)',(empno,name,gender,salary,dept))
elif choice == 2:
	mycursor.execute("desc emp")
	myrecords=mycursor.fetchall()
	for x in myrecords:
		print(x)
mydb.close()


