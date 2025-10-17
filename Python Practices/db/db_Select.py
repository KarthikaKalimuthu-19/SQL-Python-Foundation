import pyodbc

driver_name='SQL Server'
server='KARTHIKA\SQLEXPRESS'
database='python_training'

con_str=f'Driver={driver_name};Server={server};Database={database};Trusted_connection=yes;'

try:         
    con=pyodbc.connect(con_str)
    cursor=con.cursor()
    str1="select * from students"
    cursor.execute(str1)
    res=cursor.fetchall()
    for i in res:
        print(i)

except Exception as e:
    print('Error :',e)
