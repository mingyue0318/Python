#!/usr/bin/python3

import pymysql

db = pymysql.connect('localhost','root','yao123456','test')

cursor = db.cursor()
# 更新语句
sql = "UPDATE EMPLOYEE SET AGE = AGE+1 WHERE SEX = '%c'"%('M')

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()