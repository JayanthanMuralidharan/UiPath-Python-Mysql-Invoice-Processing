import mysql.connector
import pyautogui


# connecting to mysql
database = mysql.connector.connect(host='localhost', user='root', password='Developer')

# preparing a cursor object
cursorObject = database.cursor()

# Creating Database
cursorObject.execute("CREATE DATABASE uipath")
pyautogui.alert("Database Created successfully")
# closing database
database.close()
