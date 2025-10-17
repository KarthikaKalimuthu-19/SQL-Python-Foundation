import sys
sys.path.append(r'C:\Users\ELCOT\Desktop\Order_management')

import unittest
from entity.Users import Users
from entity.Clothing import Clothing
from dao.OrderProcessor import OrderProcessor

class TestOrderProcessor(unittest.TestCase):
    def test_create_order_success(self):
        user = Users(106, "karthika", "pass123", "User")
        product = Clothing(6, "Kurti", "Cotton", 999.0, 20, "M", "Blue")

        processor = OrderProcessor()
        result = processor.createOrder(user, [product])

        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
