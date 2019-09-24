import pandas as pd
import mysql.connector

def add_new_tool(cursor,file):
    tool_name,code,quantity,location = input('enter tool name:-> '),int(input('enter tool code:-> ')),int(input("enter tool quantity")),input("enter tool location:-> ")
    sql ="""insert into tool(tools,code,quantity,location) values('%s',%s,%s,'%s')"""%(tool_name,code,quantity,location)
    cursor.execute(sql)

def tool_transfer():
    pass

def tool_info():
    pass

#file_loc = input("please enter file path:-> ")
#username = input("please enter username-> ")
#dbname = input("please enter databse name-> ")
#password = input("please enter password-> ")


#connecting to databasae
db = mysql.connector.connect(host="localhost",user='root',passwd='very_strong_password',database='tool_list')
#creating cursor
cursor = db.cursor()

#reading excel file
file = pd.read_excel('/home/raman/Documents/coding_files/tool_management_app/sample_data/tool_list.xlsx')


#inserting data in database
#for i in file.index:
#    sql = f"""insert into tools(tools,code,quantity,location) values('%s', %s, %s, '%s')"""%(file['Tools'][i],file['CODE'][i],file['Quantity'][i],file['location'][i])
#    cursor.execute(sql)
db.commit() 
   