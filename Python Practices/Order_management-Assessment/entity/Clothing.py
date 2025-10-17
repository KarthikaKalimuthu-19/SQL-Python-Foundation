#--Clothing Table
import sys
sys.path.append(r'C:\Users\ELCOT\Desktop\Order_management')

from entity.Product import Product

class Clothing(Product):
    def __init__(self,productid,productName,description,price,quantityInStock,size,color):
        super().__init__(productid,productName,description,price,quantityInStock,'Clothing')
        self.size=size
        self.color=color
