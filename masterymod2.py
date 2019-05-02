'''
Name: Rohit Nachaloor
Date: 05/01/2019
Mastery Project
Period: 1
Cowart
'''

#allows for SQL queries to be performed within IDLE
import mysql.connector

def place():

    #establishes connection to the database
    dbGrade = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='123456',
        database='grades'
    )

    mycursor = dbGrade.cursor()

    print('Which class do you want to access')

    className = input()
    
    print('How many grades you need to add')
    graNum = int(input())
    #Loop that adds grades to the database
    while (graNum > 0):
        print('Please title your assignment')
        title = input()
        print('Which catagory do you need to add a grade in?')
        graCat = input()
        print('What is the grade on the assignment?')
        grade = int(input())
        sql = 'INSERT INTO '+str(className)+' (description, catagory, grade) VALUES (%s, %s, %s)'
        val = (title, graCat, str(grade))
        mycursor.execute(sql, val)
        dbGrade.commit()
        print('Grade Added')
        graNum = graNum - 1



        
