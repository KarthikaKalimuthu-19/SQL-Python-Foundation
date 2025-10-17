import unittest

def add(a,b):
    return a+b

c=add(2,3)
print(c)


#--apply pyunit

class TestAddFunction(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(10,20),30)

    def test_add_negative(self):
        self.assertEqual(add(-5,-4),-9)

    def test_add_mixed(self):
        self.assertEqual(add(-5,2),-3)

    def test_add_mixed(self):
        self.assertEqual(add(-5,0),-5)


unittest.main()        #--if we given wrong expected value then it gives asserterror and also failed
                   
