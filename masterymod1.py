'''
Name: Rohit Nachaloor
Date: 05/01/2019
Mastery Project
Period: 1
Cowart
'''

#module that allows SQL queries to be performed in IDLE
import mysql.connector as SQL
#tkinter GUI module
from tkinter import *

def setup():
    #sets up the connection to the database
    dbGrade = SQL.connect(
        host='localhost',
        user='root',
        passwd='123456',
        database='grades'
    )

    mycursor = dbGrade.cursor()

    print('How many classes you want to add?')
    amClass = int(input())
    while (amClass > 0):
        print('What is the name of the class?')
        className = input()
        #SQL query for creating a table which stores the grades
        sql = 'CREATE TABLE '+str(className)+' (id INT AUTO_INCREMENT PRIMARY KEY, description varchar(255), catagory varchar(30), grade INT)'
        mycursor.execute(sql)
        dbGrade.commit()
        print('How many catagories does this class have')
        catNum = int(input())
        #SQL query for creating the table for grade catagories and their percent values
        sql = 'CREATE TABLE '+str(className)+'Cat (id INT AUTO_INCREMENT PRIMARY KEY, catagory varchar(30), percent int)'
        mycursor.execute(sql)
        dbGrade.commit()
        #loop that adds grade catagories and percent values
        while (catNum > 0):
            print('Type the name of the catagory')
            catName = input()
            print('Type the percent of the grade')
            catPer = int(input())
            sql = 'INSERT INTO '+str(className)+'Cat (catagory, percent) VALUES (%s, %s)'
            val = (catName, str(catPer))
            mycursor.execute(sql, val)
            dbGrade.commit()
            catNum = catNum - 1
        amClass = amClass - 1
        print('Your class was created.')

