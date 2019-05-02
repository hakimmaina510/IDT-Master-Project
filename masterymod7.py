'''
Name: Rohit Nachaloor
Date Submitted: 05/01/2019
Mastery Project
Period: 1
Cowart
'''
import mysql.connector as SQL
from smtplib import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def mail():
    dbGrade = SQL.connect(
        host='localhost',
        user='root',
        passwd='123456',
        database='grades'
    )

    mycursor = dbGrade.cursor()

    #asks user about their email address
    print('What is your email address?')
    send_email = input()
    #writes email into text file
    gradeTEXT = open('gradesTEXT.txt', 'w')
    gradeTEXT.write(send_email+'\n')
    gradeTEXT.close()
    print('How many classes are we emailing')
    classNum = int(input())
    xClassNum = 0
    while (xClassNum < classNum):
        #asks and writes class name into text file
        print('Which class do you want your grades emailed?')
        className = input()
        gradeTEXT = open('gradesTEXT.txt', 'a')
        gradeTEXT.write('\n' + className)
        gradeTEXT.close()
        sql = 'SELECT * FROM '+className
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:
            #puts all grade info into text file
            gradeTEXT = open('gradesTEXT.txt', 'a')
            gradeTEXT.write("Assignment No. = "+str(x[0])+'\n')
            gradeTEXT.close()
            gradeTEXT = open('gradesTEXT.txt', 'a')
            gradeTEXT.write("Assignment Name = "+x[1]+'\n')
            gradeTEXT.close()
            gradeTEXT = open('gradesTEXT.txt', 'a')
            gradeTEXT.write("Catagory  = "+x[2]+'\n')
            gradeTEXT.close()
            gradeTEXT = open('gradesTEXT.txt', 'a')
            gradeTEXT.write("Grade  = "+str(x[3])+"\n\n")
            gradeTEXT.close()
        xCatNum = 1
        # sql command to count the types of grades
        sql = 'SELECT COUNT(id) FROM ' + str(className) + 'cat;'
        mycursor.execute(sql)
        myresult = mycursor.fetchone()
        CATNUM = myresult
        catNUM = str(CATNUM)
        CATnum = catNUM.strip('(')
        catNum = int(CATnum.strip(',)'))
        calcList = []
        # if statement will be enacted depending on the amount of catagories.
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
        #writes average into text file
        gradeTEXT = open('gradesTEXT.txt', 'a')
        gradeTEXT.write('Your average is:'+str(average)+'%')
        gradeTEXT.close()
        xClassNum = xClassNum + 1
    subject = 'Your Grade Package'
    email_user = 'nachaloortest@gmail.com'
    email_password = 'test123$'
    #sets up email parameters (i.e. subject, sender email, reciever email)
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_password
    msg['Subject'] = subject
    body = 'This is your requested grade package'
    #sets up body parameters
    msg.attach(MIMEText(body,'plain'))
    #this section opens and attaches text file to email
    filename = 'gradesTEXT.txt'
    attachment = open(filename, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition','attachment; filename= '+filename)
    msg.attach(part)
    TEXT = msg.as_string()
    #sets up connection to gmail
    server = SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user, email_password)
    #sends email
    server.sendmail(email_user, send_email, TEXT)
    server.quit()
    print('Email Sent')
