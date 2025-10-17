import pyodbc

import sys
sys.path.append(r'C:\Users\ELCOT\Desktop\Order_management')

from utill.PropertyUtil import PropertyUtil

class DBConnUtil:
    @staticmethod
    def get_connection():
        connection_string=PropertyUtil.get_property_string()
        return pyodbc.connect(connection_string)

