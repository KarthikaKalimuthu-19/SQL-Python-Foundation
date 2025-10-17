from abc import ABC, abstractmethod

import sys
sys.path.append(r'C:\Users\ELCOT\Desktop\Finance')

from entity.Users import Users
from entity.Expenses import Expenses
from entity.ExpenseCategories import ExpenseCategories

class IFinanceRepository(ABC):
    @abstractmethod
    def createUser(self,user: Users):
        pass

    @abstractmethod
    def createExpense(self,expense: Expenses):
        pass
    
    @abstractmethod
    def deleteUser(self,user_id: int):
        pass

    @abstractmethod
    def deleteExpense(self,expense_id: int):
        pass

    @abstractmethod
    def getAllExpenses(self,user_id: int):
        pass

    @abstractmethod
    def updateExpense(self,user_id: int,expense: Expenses):
        pass
