#--Electronics Table
import sys
sys.path.append(r'C:\Users\ELCOT\Desktop\Order_management')

from entity.Product import Product

class Electronics(Product):
    def __init__(self,productid,productName,description,price,quantityInStock,brand,warranty_period):
        super().__init__(productid,productName,description,price,quantityInStock,'Electronics')
        self.brand=brand
        self.warranty_period=warranty_period
