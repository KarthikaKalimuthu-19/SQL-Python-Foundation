import unittest

str1='computer'
str2='HEXAWARE'

#--apply pyunit

class TestString(unittest.TestCase):
    def testStringUpper(self):
        self.assertTrue(str2.isupper())

    def testStringUpper1(self):
        self.assertTrue(str1.isupper())

    def testStringUpper_false(self):
        self.assertFalse(str1.isupper())

    def testStringUpper_true(self):
        self.assertFalse(str2.isupper())

    def testStringLower(self):
        self.assertTrue(str1.islower())

    def testStringLower_false(self):
        self.assertFalse(str2.islower())


unittest.main()
