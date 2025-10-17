import sys
sys.path.append(r'C:\Users\ELCOT\Desktop\Finance')

from dao.IFinanceRepository import IFinanceRepository

from utill.DBConnUtil import DBConnUtil
from utill.PropertyUtil import PropertyUtil

from exception.UserNotFoundException import UserNotFoundException
from exception.ExpenseNotFoundException import ExpenseNotFoundException

from entity.Users import Users
from entity.Expenses import Expenses
from entity.ExpenseCategories import ExpenseCategories


class FinanceRepositoryImpl(IFinanceRepository):
    def __init__(self):
        self.connection = DBConnUtil.get_connection()

    def createUser(self,user: Users):
        cursor=self.connection.cursor()
        
        try:
            cursor.execute('insert into Users(user_id, username, password, email) values (?,?,?,?)',
                (user.user_id, user.username, user.password, user.email))
            self.connection.commit()
            return True

        except Exception as e:
            print(f'Error inserting User: {e}')
            return False
                  

    def createExpense(self,expense: Expenses):
        cursor=self.connection.cursor()

        try:
            cursor.execute('insert into Expenses(expense_id, user_id,amount,category_id,date,description) values (?,?,?,?,?,?)',
                (expense.expense_id, expense.user_id, expense.amount, expense.category_id, expense.date, expense.description))
            self.connection.commit()
            return True

        except Exception as e:
            print(f'Error in inserting Expense: {e}')
            return False


    def deleteUser(self, user_id: int):
        cursor=self.connection.cursor()

        try:
            cursor.execute('select * from Users where user_id=?',(user_id))
            if not cursor.fetchone():
                raise UserNotFoundException(f'User with ID {user_id} does not exist.')

            cursor.execute('delete from Users where user_id=?',(user_id))
            self.connection.commit()
            return True

        except UserNotFoundException as ue:
            print(ue)
            return False

        except Exception as e:
            print(f'Error deleting User: {e}')
            return False
        

    def deleteExpense(self,expense_id: int):
        cursor=self.connection.cursor()

        try:
            cursor.execute('select * from Expenses where expense_id=?',(expense_id))
            if not cursor.fetchone():
                raise ExpenseNotFoundException(f'Expense with ID {expense_id} does not exist.')

            cursor.execute('delete from Expenses where expense_id=?',(expense_id))
            self.connection.commit()
            return True

        except ExpenseNotFoundException as ee:
            print(ee)
            return False

        except Exception as e:
            print(f'Error in deleting Expense: {e}')
            return False
        

    def getAllExpenses(self,user_id: int):
        cursor=self.connection.cursor()

        try:
            cursor.execute('select * from Expenses where user_id=?',(user_id))
            if not cursor.fetchone():
                raise UserNotFoundException(f'User with ID {user_id} does not exist.')

            cursor.execute('select * from Expenses where user_id=?',(user_id))
            rows=cursor.fetchall()
            return [Expenses(*row) for row in rows]

        except UserNotFoundException as ue:
            print(ue)
            return []

        except Exception as e:
            print(f'Error in retrieving expenses: {e}')
            return []
        

    def updateExpense(self,user_id: int,expense: Expenses):
        cursor=self.connection.cursor()

        try:
            cursor.execute('select * from Expenses where expense_id=? and user_id=?',(expense.expense_id,user_id))
            if not cursor.fetchone():
                raise ExpenseNotFoundException(f'Expense with ID {expense.expense_id} for User {user_id} not found.')

            cursor.execute('update Expenses set amount=?, category_id=?, date=?, description=? where expense_id=? and user_id=?',
                     (expense.amount,expense.category_id,expense.date,expense.description,expense.expense_id,user_id))
            self.connection.commit()
            return True

        except ExpenseNotFoundException as ee:
            print(ee)
            return False

        except Exception as e:
            print(f'Error in updating expense: {e}')
            return False








        
        
