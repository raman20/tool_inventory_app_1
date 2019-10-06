# -*- coding: utf-8 -*-
import mysql.connector
import os
from openpyxl import Workbook


def to_excel(result,cursor):
   pass

def add_new_tool():
    n = int(input('how many tools to add:-> '))
    db = mysql.connector.connect(host='localhost',user='root',passwd='very_strong_password',database='tool_list')   
    cursor = db.cursor()
    while(n>0):
        tool_name,code,quantity,location = input('enter tool name:-> '),int(input('enter tool code:-> ')),int(input("enter tool quantity")),input("enter tool location:-> ")
        sql =f"""insert into tools(tools,code,quantity,location) values('{tool_name}',{code},{quantity},'{location}')"""
        cursor.execute(sql)
        n-=1
    print("tool added")
    cursor.close()
    db.commit()
    db.close()
    print("close")
    ''' mode = input("press 'y' if u have excel data:-> ")
    if lower(mode) == 'y':
       file_path = input('enter the file path:-> ')
       file = pd.read_excel(file_path)
       for i in file.index:
           sql = """insert into tools(tools,code,quantity,location) values('%s',%s,%s,'%s')"""%()'''

def tool_transfer():
    db = mysql.connector.connect(host='localhost',user='root',passwd='very_strong_password',database='tool_list')
    cursor = db.cursor()
    n = int(input("how many tools need to send:-> "))
    #origrin = input("enter present location:-> ")
    destination = input("enter destination:-> ")
    while(n>0):
        code = int(input("enter tool code:-> "))
        quantity = int(input("enter quantity:-> "))
        #updating in main database
        sql = f"update tools set quantity=quantity-{quantity},location='{destination}' where code={code}"
        cursor.execute(sql)
        n-=1
    #fetching the transfered tool data
    db.commit()
    sql = f"select * from tools where location='{destination}'"
    cursor.execute(sql)  
    result = cursor.fetchall()
    sheetname = input('enter sheet name:-> ')
    path = 'save_data/'+ sheetname +'.xlsx'
    # saving data to excel file
    wb = Workbook()
    ws = wb.create_sheet(0)
    ws.title = sheetname
    ws.append(cursor.column_names)
    for i in result:
        ws.append(i)
    os.mknod(path) # create new excel file
    wb.save(path)    
    wb.close()
    print(f'data exported to excel_file at "{path}"')
    cursor.close()
    db.close()
    

def tool_status():
    db = mysql.connector.connect(host='localhost',user='root',passwd='very_strong_password',database='tool_list')
    cursor = db.cursor()
    code = int(input('enter tool code:-> '))
    sql = f"select * from tools where code={code}"
    cursor.execute(sql)
    for i in cursor:
        print(i)
    cursor.close()
    db.close()