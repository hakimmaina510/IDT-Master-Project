'''
Name: Rohit Nachaloor
Date: 04/05/2019
Mastery Project
Period: 1
Cowart
'''

import mysql.connector as SQL

def final():
    #establishes connection to database
    dbGrade = SQL.connect(
        host='localhost',
        user='root',
        passwd='123456',
        database='grades'
    )

    mycursor = dbGrade.cursor()

    #user inputs class they want to
    print('Which class do you want to test your final grade.')
    className = input()
    #sql query for the getting the total weight of all the catagorys
    sql = 'SELECT SUM(percent) FROM '+className+'cat;'
    mycursor.execute(sql)
    myresult = mycursor.fetchone()
    totPer = myresult
    totPer = str(totPer)
    totPer = totPer.strip("(Decimal'")
    totPer = int(float(totPer.strip("'),)")))
    xCatNum = 1
    #sql query for counting the amount of categories in a class
    sql = 'SELECT COUNT(id) FROM '+str(className)+'cat;'
    mycursor.execute(sql)
    myresult = mycursor.fetchone()
    CATNUM = myresult
    catNUM = str(CATNUM)
    CATnum = catNUM.strip('(')
    catNum = int(CATnum.strip(',)'))
    calcList = []
    calcTot = lambda x, y, z : x + y + z
    #if statements dependent on the amount of the number of grade categories
    if (catNum == 2):
        while (xCatNum < 3):
            #sql statement that collects the names of the categories
            sql = 'SELECT catagory FROM '+str(className)+'cat WHERE id = '+str(xCatNum)
            mycursor.execute(sql)
            myresult = mycursor.fetchone()
            CAT = myresult
            caT = str(CAT)
            CaT = caT.strip('(')
            cat = CaT.strip(',)')
            #sql query that counts the amount of grades in a catagory
            sql = 'SELECT COUNT(grade) FROM '+str(className)+' WHERE catagory = '+str(cat)
            mycursor.execute(sql)
            myresult = mycursor.fetchone()
            y = myresult
            #sql query that averages the grades in a certain category
            sql = 'SELECT AVG(grade) FROM '+str(className)+' WHERE catagory = '+str(cat)
            mycursor.execute(sql)
            myresult = mycursor.fetchone()
            gradeAvg = str(myresult)
            gradeAvg = gradeAvg.strip("(Decimal'")
            gradeAvg = int(float(gradeAvg.strip("'),)")))
            #sql query that gets the percent of grade that a category takes up
            sql = 'SELECT percent FROM '+str(className)+'cat WHERE catagory = '+str(cat)
            mycursor.execute(sql)
            myresult = mycursor.fetchone()
            res = str(myresult)
            res = res.strip('(')
            res = int(res.strip(',)'))
            #lambda function that calculates the weighted portion of a category
            catCalc = lambda x, y : x * (y / 100)
            #the previous value is being added to a list.
            calcList.append(catCalc(gradeAvg, res))
            xCatNum = xCatNum + 1
        #gives final exam weight
        finalWeig = 100 - totPer
        #asks for desired final exam grade
        print('What do you want on the final exam.')
        gradeWish = int(input())
        wishWeight = (finalWeig / 100) * gradeWish
        #lambda that calculates the average with the desired final exam grade
        finalCalc = lambda x, y, z : ((x + y + z) / 100) * 100
        average = finalCalc(int(calcList[0]), int(calcList[1]), wishWeight)
        print(average)
    if (catNum == 3):
        while (xCatNum < 4):
            #sql statement that collects the names of the categories
            sql = 'SELECT catagory FROM '+str(className)+'cat WHERE id = '+str(xCatNum)
            mycursor.execute(sql)
            myresult = mycursor.fetchone()
            CAT = myresult
            caT = str(CAT)
            CaT = caT.strip('(')
            cat = CaT.strip(',)')
            #sql query that counts the amount of grades in a catagory
            sql = 'SELECT COUNT(grade) FROM '+str(className)+' WHERE catagory = '+str(cat)
            mycursor.execute(sql)
            myresult = mycursor.fetchone()
            y = myresult
            #sql query that averages the grades in a certain category
            sql = 'SELECT AVG(grade) FROM '+str(className)+' WHERE catagory = '+str(cat)
            mycursor.execute(sql)
            myresult = mycursor.fetchone()
            gradeAvg = str(myresult)
            gradeAvg = gradeAvg.strip("(Decimal'")
            gradeAvg = int(float(gradeAvg.strip("'),)")))
            #sql query that gets the percent of grade that a category takes up
            sql = 'SELECT percent FROM '+str(className)+'cat WHERE catagory = '+str(cat)
            mycursor.execute(sql)
            myresult = mycursor.fetchone()
            res = str(myresult)
            res = res.strip('(')
            res = int(res.strip(',)'))
            #lambda function that calculates the weighted portion of a category
            catCalc = lambda x, y : x * (y / 100)
            calcList.append(catCalc(gradeAvg, res))
            xCatNum = xCatNum + 1
        #gives final exam weight
        finalWeig = 100 - totPer
        print('What do you want on the final exam.')
        gradeWish = int(input())
        wishWeight = (finalWeig / 100) * gradeWish
        # lambda that calculates the average with the desired final exam grade
        finalCalc = lambda w, x, y, z : ((w + x + y + z) / 100) * 100
        average = finalCalc(int(calcList[0]), int(calcList[1]), int(calcList[2]), wishWeight)
        print(average)
    if (catNum == 4):
        while (xCatNum < 5):
            #sql statement that collects the names of the categories
            sql = 'SELECT catagory FROM '+str(className)+'cat WHERE id = '+str(xCatNum)
            mycursor.execute(sql)
            myresult = mycursor.fetchone()
            CAT = myresult
            caT = str(CAT)
            CaT = caT.strip('(')
            cat = CaT.strip(',)')
            #sql query that counts the amount of grades in a catagory
            sql = 'SELECT COUNT(grade) FROM '+str(className)+' WHERE catagory = '+str(cat)
            mycursor.execute(sql)
            myresult = mycursor.fetchone()
            y = myresult
            #sql query that averages the grades in a certain category
            sql = 'SELECT AVG(grade) FROM '+str(className)+' WHERE catagory = '+str(cat)
            mycursor.execute(sql)
            myresult = mycursor.fetchone()
            gradeAvg = str(myresult)
            gradeAvg = gradeAvg.strip("(Decimal'")
            gradeAvg = int(float(gradeAvg.strip("'),)")))
            #sql query that gets the percent of grade that a category takes up
            sql = 'SELECT percent FROM '+str(className)+'cat WHERE catagory = '+str(cat)
            mycursor.execute(sql)
            myresult = mycursor.fetchone()
            res = str(myresult)
            res = res.strip('(')
            res = int(res.strip(',)'))
            #lambda function that calculates the weighted portion of a category
            catCalc = lambda x, y : x * (y / 100)
            calcList.append(catCalc(gradeAvg, res))
            xCatNum = xCatNum + 1
        #gives final exam weight
        finalWeig = 100 - totPer
        print('What do you want on the final exam.')
        gradeWish = int(input())
        wishWeight = (finalWeig / 100) * gradeWish
        # lambda that calculates the average with the desired final exam grade
        finalCalc = lambda v, w, x, y, z : ((v + w + x + y + z) / 100) * 100
        average = finalCalc(int(calcList[0]), int(calcList[1]), int(calcList[2]), int(calcList[3]), wishWeight)
        print(average)
