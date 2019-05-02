'''
Name: Rohit Nachaloor
Date: 04/05/2019
Mastery Project
Period: 1
Cowart
'''

import mysql.connector as SQL

dbGrade = SQL.connect(
    host='localhost',
    user='root',
    passwd='123456',
    database='grades'
)

#SQL
select * from test;
