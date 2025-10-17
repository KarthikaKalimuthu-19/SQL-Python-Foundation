#--OrderItems table

class OrderItems:
    def __init__(self,order_item_id,order_id,productid,quantity):
        self.order_item_id=order_item_id
        self.order_id=order_id
        self.productid=productid
        self.quantity=quantity
