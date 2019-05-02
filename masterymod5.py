'''
Name: Rohit Nachaloor
Date: 05/01/2019
Mastery Project
Period: 1
Cowart
'''

import mysql.connector as SQL

def view():
    dbGrade = SQL.connect(
        host='localhost',
        user='root',
        passwd='123456',
        database='grades'
    )

    mycursor = dbGrade.cursor()

    #gets user input to see grades
    print('Which class do you want to see your grades.')
    className = input()
    #sql query to get all information concerning grades in a class
    sql = 'SELECT * FROM '+className
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    #organizes results in a readable fashion
    for x in myresult:
       print("Assignment No. = ", x[0], )
       print("Assignment Name = ", x[1])
       print("Catagory  = ", x[2])
       print("Grade  = ", x[3], "\n")

    
    

