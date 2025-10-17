import pyodbc

driver_name='SQL Server'
server='KARTHIKA\\SQLEXPRESS'
database='python_training'

con_str=f'Driver={driver_name};Server={server};Database={database};Trusted_connection=yes;'

try:
  con=pyodbc.connect(con_str)
  cursor=con.cursor()
  str1="insert into students values(8,'karthika','Erode')"
  cursor.execute(str1)
  cursor.commit()
  print('Inserted value in students table')

except Exception as e:
    print('Error :',e)
