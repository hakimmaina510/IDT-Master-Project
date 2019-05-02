'''
Name: Rohit Nachaloor
Date: 05/01/2019
Mastery Project
Period: 1
Cowart
'''

import mysql.connector as SQL

def test():
    dbGrade = SQL.connect(
        host='localhost',
        user='root',
        passwd='123456',
        database='grades'
    )

    mycursor = dbGrade.cursor()
    #asks user about what class they want.
    print('Which class do you want to test your average in?')
    className = input()
    print('What catagory is this to be added from?')
    testCat = input()
    xCatNum = 1
    print('What did you get on the assignment?')
    testGrade = input()
    # sql command to count the types of grades
    sql = 'SELECT COUNT(id) FROM ' + str(className) + 'cat;'
    mycursor.execute(sql)
    myresult = mycursor.fetchone()
    CATNUM = myresult
    catNUM = str(CATNUM)
    CATnum = catNUM.strip('(')
    catNum = int(CATnum.strip(',)'))
    calcList = []
    print(catNum)
    sql = 'INSERT INTO ' + str(className) + ' (catagory, grade) VALUES (%s, %s)'
    val = (testCat, testGrade)
    mycursor.execute(sql, val)
    if (catNum == 2):
        # loop that gets weighted total from each catagory
        while (xCatNum < 3):
            sql = 'SELECT catagory FROM ' + str(className) + 'cat WHERE id = ' + str(xCatNum)
            mycursor.execute(sql)
            myresult = mycursor.fetchone()
            CAT = myresult
            caT = str(CAT)
            CaT = caT.strip('(')
            cat = CaT.strip(',)')
            sql = 'SELECT COUNT(grade) FROM ' + str(className) + ' WHERE catagory = ' + str(cat)
            mycursor.execute(sql)
            myresult = mycursor.fetchone()
            y = myresult
            sql = 'SELECT AVG(grade) FROM ' + str(className) + ' WHERE catagory = ' + str(cat)
            mycursor.execute(sql)
            myresult = mycursor.fetchone()
            gradeAvg = str(myresult)
            gradeAvg = gradeAvg.strip("(Decimal'")
            gradeAvg = int(float(gradeAvg.strip("'),)")))
            sql = 'SELECT percent FROM ' + str(className) + 'cat WHERE catagory = ' + str(cat)
            mycursor.execute(sql)
            myresult = mycursor.fetchone()
            res = str(myresult)
            res = res.strip('(')
            res = int(res.strip(',)'))
            catCalc = lambda x, y: x * (y / 100)
            calcList.append(catCalc(gradeAvg, res))
            xCatNum = xCatNum + 1
        # SQL query that gets total weight
        sql = 'SELECT SUM(percent) FROM ' + str(className) + 'cat'
        mycursor.execute(sql)
        myresult = mycursor.fetchone()
        totWeigh = str(myresult)
        totWeigh = totWeigh.strip("(Decimal'")
        totWeigh = int(float(totWeigh.strip("'),)")))
        # lambda function that will calculate the average
        avgCalc = lambda x, y, z: ((x + y) / z) * 100
        average = avgCalc(int(calcList[0]), int(calcList[1]), int(totWeigh))
        print('Your average is: ' + str(average) + '%')

    if (catNum == 3):
        # loop that gets weighted total from each catagory
        while (xCatNum < 4):
            sql = 'SELECT catagory FROM ' + str(className) + 'cat WHERE id = ' + str(xCatNum)
            mycursor.execute(sql)
            myresult = mycursor.fetchone()
            CAT = myresult
            caT = str(CAT)
            CaT = caT.strip('(')
            cat = CaT.strip(',)')
            sql = 'SELECT COUNT(grade) FROM ' + str(className) + ' WHERE catagory = ' + str(cat)
            mycursor.execute(sql)
            myresult = mycursor.fetchone()
            y = myresult
            sql = 'SELECT AVG(grade) FROM ' + str(className) + ' WHERE catagory = ' + str(cat)
            mycursor.execute(sql)
            myresult = mycursor.fetchone()
            gradeAvg = str(myresult)
            gradeAvg = gradeAvg.strip("(Decimal'")
            gradeAvg = int(float(gradeAvg.strip("'),)")))
            sql = 'SELECT percent FROM ' + str(className) + 'cat WHERE catagory = ' + str(cat)
            mycursor.execute(sql)
            myresult = mycursor.fetchone()
            res = str(myresult)
            res = res.strip('(')
            res = int(res.strip(',)'))
            catCalc = lambda x, y: x * (y / 100)
            calcList.append(catCalc(gradeAvg, res))
            xCatNum = xCatNum + 1
        # SQL query that gets the total weight
        sql = 'SELECT SUM(percent) FROM ' + str(className) + 'cat'
        mycursor.execute(sql)
        myresult = mycursor.fetchone()
        totWeigh = str(myresult)
        totWeigh = totWeigh.strip("(Decimal'")
        totWeigh = int(float(totWeigh.strip("'),)")))
        # function that calculated the average
        avgCalc = lambda w, x, y, z: ((w + x + y) / z) * 100
        average = avgCalc(int(calcList[0]), int(calcList[1]), int(calcList[2]), int(totWeigh))
        print('Your average is: ' + str(average) + '%')

    if (catNum == 4):
        # loop that gets weighted total from each catagory
        while (xCatNum < 5):
            sql = 'SELECT catagory FROM ' + str(className) + 'cat WHERE id = ' + str(xCatNum)
            mycursor.execute(sql)
            myresult = mycursor.fetchone()
            CAT = myresult
            caT = str(CAT)
            CaT = caT.strip('(')
            cat = CaT.strip(',)')
            sql = 'SELECT COUNT(grade) FROM ' + str(className) + ' WHERE catagory = ' + str(cat)
            mycursor.execute(sql)
            myresult = mycursor.fetchone()
            y = myresult
            sql = 'SELECT AVG(grade) FROM ' + str(className) + ' WHERE catagory = ' + str(cat)
            mycursor.execute(sql)
            myresult = mycursor.fetchone()
            gradeAvg = str(myresult)
            gradeAvg = gradeAvg.strip("(Decimal'")
            gradeAvg = int(float(gradeAvg.strip("'),)")))
            sql = 'SELECT percent FROM ' + str(className) + 'cat WHERE catagory = ' + str(cat)
            mycursor.execute(sql)
            myresult = mycursor.fetchone()
            res = str(myresult)
            res = res.strip('(')
            res = int(res.strip(',)'))
            catCalc = lambda x, y: x * (y / 100)
            calcList.append(catCalc(gradeAvg, res))
            xCatNum = xCatNum + 1
        # SQL query that gets total weight
        sql = 'SELECT SUM(percent) FROM ' + str(className) + 'cat'
        mycursor.execute(sql)
        myresult = mycursor.fetchone()
        totWeigh = str(myresult)
        totWeigh = totWeigh.strip("(Decimal'")
        totWeigh = int(float(totWeigh.strip("'),)")))
        # function that calculates average
        avgCalc = lambda v, w, x, y, z: ((v + w + x + y) / z) * 100
        average = avgCalc(int(calcList[0]), int(calcList[1]), int(calcList[2]), int(calcList[3]), int(totWeigh))
        print('Your average is: ' + str(average) + '%')

