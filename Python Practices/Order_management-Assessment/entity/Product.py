#--Product Table

class Product:
    def __init__(self,productid,productName,description,price,quantityInStock,type):
        self.productid=productid
        self.productName=productName
        self.description=description
        self.price=price
        self.quantityInStock=quantityInStock
        self.type=type
