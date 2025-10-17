import sys
sys.path.append(r'C:\Users\ELCOT\Desktop\Order_management')

from abc import ABC, abstractmethod

from entity.Users import Users
from entity.Orders import Orders
from entity.Product import Product
from entity.OrderItems import OrderItems


class IOrderManagementRepository(ABC):
    
    @abstractmethod
    def createOrder(self,user: Users, product: list[Product]):
        pass

    @abstractmethod
    def getOrderByUser(self,user: Users):
        pass

