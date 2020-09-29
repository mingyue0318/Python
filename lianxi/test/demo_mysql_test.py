#!/usr/bin/python3
import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",     
    user= "root",
    password="Yy.0318!"
)

print(mydb)