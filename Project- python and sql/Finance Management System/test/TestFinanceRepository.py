import sys
sys.path.append(r'C:\Users\ELCOT\Desktop\Finance')

import unittest

from dao.FinanceRepositoryImpl import FinanceRepositoryImpl
from entity.Users import Users
from entity.Expenses import Expenses
from entity.ExpenseCategories import ExpenseCategories


class TestFinanceRepository(unittest.TestCase):

    def test_createUser(self):
        repo = FinanceRepositoryImpl()
        user = Users (3,'ramya','lkjhgfdsa','ramya@example.com')
        result = repo.createUser(user)
        self.assertTrue(result)

    def test_createExpense(self):
        repo = FinanceRepositoryImpl()
        expense = Expenses (108,4,5000.00,3,'2025-06-25','montly rent')
        result = repo.createExpense(expense)
        self.assertTrue(result)

    def test_deleteUser(self):
        repo = FinanceRepositoryImpl()
        user_id = 7
        result = repo.deleteUser(user_id)
        self.assertTrue(result)

    def test_deleteExpense(self):
        repo = FinanceRepositoryImpl()
        expense_id = 108
        result = repo.deleteExpense(expense_id)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
    










        
        
