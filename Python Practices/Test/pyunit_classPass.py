import unittest

class employee:
    pass

obj1=employee()
obj2=employee()
obj3=obj1

#--Apply pyunit with Testcases

class TeatClass(unittest.TestCase):
    def test_obj(self):
        self.assertIs(obj1,obj3)

    def test_objNot(self):
        self.assertIsNot(obj1,obj2)

    def test_obj(self):
        self.assertIs(obj1,obj2)

unittest.main()
