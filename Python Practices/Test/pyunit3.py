import unittest

str1='computer'
str2='HEXAWARE'
str3='computer'
str4='cse it'
#str5='cse it'

#--apply pyunit

class TestString(unittest.TestCase):
    def testStringEqual(self):
        self.assertEqual(str1,str3)

    def testStringEqualnegative(self):
        self.assertEqual(str1,str2)

    def testStringSplit(self):
        self.assertEqual(str4.split(),['cse','it'])


unittest.main()
