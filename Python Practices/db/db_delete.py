import pyodbc

driver_name='SQL Server'
server='KARTHIKA\SQLEXPRESS'
database='python_training'

con_str=f'Driver={driver_name};Server={server};Database={database};Trusted_connection=yes;'

try:
    #print('Enter student info')
    #sid=int(input('Enter student ID :'))
    #sname=input('Enter student name :')
    #saddress=input('Enter address :')
            
    con=pyodbc.connect(con_str)
    cursor=con.cursor()
    str1="delete from students where id=8"
    cursor.execute(str1)
    cursor.commit()
    print('Data deleted in students table')

except Exception as e:
    print('Error :',e)
