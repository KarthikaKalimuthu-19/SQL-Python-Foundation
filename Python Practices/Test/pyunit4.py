import unittest

marks=[80,90,100]
dept='cse it ece eee mech civil'

#--apply pyunit

class Test(unittest.TestCase):
    def test_elementIn_positive(self):
        self.assertIn(90,marks)

    def test_elementIn_negative(self):
        self.assertIn(65,marks)

    def test_stringElement_positive(self):
        self.assertIn('eee',dept)
        self.assertIn('cse',dept)
        self.assertIn('ece',dept)

    def test_stringElement_negative(self):
        self.assertIn('accounts',dept)
        self.assertIn('commerce',dept)
        self.assertIn('aids',dept)

    def test_sNOTIn(self):
        self.assertNotIn('accounts',dept)
        self.assertNotIn('cse',dept)



unittest.main()
