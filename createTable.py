import mysql.connector as SQLC
import pyautogui


def CreateTable():
    # Connecting To the Database in Localhost
    Database = SQLC.connect(host='localhost', user='root', password='Developer', database='uipath')
    # Cursor to the database
    Cursor = Database.cursor()
    # Creating Table
    # Creating Table
    records = """CREATE TABLE INVOICES(
                 INVOICE_NO VARCHAR(20) NOT NULL,
                 CUSTOMER_ID VARCHAR(20) NOT NULL,
                 NAME VARCHAR(255) NOT NULL,
                 TOTAL_AMOUNT VARCHAR(6)
                 )"""
    Cursor.execute(records)
    

pyautogui.alert("Table has been created")
CreateTable()
