import pyodbc

import sys
sys.path.append(r'C:\Users\ELCOT\Desktop\Finance')

driver_name='SQL Server'
server='KARTHIKA\\SQLEXPRESS'
database='Finance'

class PropertyUtil:
    @staticmethod
    def get_property_string():
        connection_string=f'Driver={driver_name};Server={server};Database={database};Trusted_connection=yes;'
        return connection_string
