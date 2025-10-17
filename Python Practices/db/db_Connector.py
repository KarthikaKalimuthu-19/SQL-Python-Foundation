import pyodbc

driver_name='SQL Server'
server='KARTHIKA\\SQLEXPRESS'
database='python_training'

con_str=f'Driver={driver_name};Server={server};Database={database};Trusted_connection=yes;'

con=pyodbc.connect(con_str)
print(con)  
