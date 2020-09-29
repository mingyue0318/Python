#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import pymysql

db = pymysql.connect('localhost','root','yao123456','test')

cursor = db.cursor()

sql = """
            SELECT * FROM EMPLOYEE \
            WHERE INCOME > %s %(1000)
      """
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]

        print('fname=%s,lname=%s,age=%s,sex=%s,income=%s'% \
            (fname,laname,age,sex,income))
except:
    print("Error:unable to fetch data")

db.close()