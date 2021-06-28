import mysql.connector as SQLC
import xlrd
import pyautogui


def InsertRecords():
    # Connecting To the Database in Localhost
    Database = SQLC.connect(host='localhost', user='root', password='Developer', database='uipath')
    # Cursor to the database
    Cursor = Database.cursor()
    # reading xls
    loc = 'output.xlsx'

    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_name('Sheet1')

    # For row 0 and column 0
    sheet.cell_value(0, 0)
    i = 1
    while i < sheet.nrows:
        records = sheet.row_values(i, 0)

        in_no = str(records[0]).strip()
        c_no = str(records[1]).strip()
        name = str(records[2]).strip()
        total = str(records[3]).strip()

        sql = "INSERT INTO invoices(INVOICE_NO,CUSTOMER_ID,NAME,TOTAL_AMOUNT) VALUES(%s,%s,%s,%s )"
        val = (in_no, c_no, name, total)
        Cursor.execute(sql, val)
        i += 1

    Database.commit()
    pyautogui.alert("Records has been inserted successfully")
    Database.close()


InsertRecords()
