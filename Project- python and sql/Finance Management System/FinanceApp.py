import sys
sys.path.append(r'C:\Users\ELCOT\Desktop\Finance')

from decimal import Decimal
from dao.FinanceRepositoryImpl import FinanceRepositoryImpl

from entity.Users import Users
from entity.Expenses import Expenses
from entity.ExpenseCategories import ExpenseCategories


def main():
    repo = FinanceRepositoryImpl()

    while True:
        print('\n-----------Finance App-------------')

        print('1. Add User')
        print('2. Add Expense')
        print('3. Delete User')
        print('4. Delete Expense')
        print('5. Get all Expenses')
        print('6. Update Expense')
        print('7. Exit')

        try:
            choice = int(input("Choose an option: "))
            
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            user_id = int(input('Enter User ID: '))
            username = input('Enter username: ')
            password = input('Enter password: ')
            email = input('Enter email: ')

            user = Users(user_id, username, password, email)

            if repo.createUser(user):
                print('User added successfully.')

            else:
                print('Failed to add User.')


        elif choice == 2:
            expense_id = int(input('Enter expense_id: '))
            user_id = int(input('Enter user ID: '))
            amount = Decimal(input('Enter amount: '))
            category_id = int(input('Enter Category ID: '))
            date = input('Enter the date(YYYY-MM-DD): ')
            description = input('Enter description: ')

            expense = Expenses(expense_id, user_id, amount, category_id, date, description)

            if repo.createExpense(expense):
                print('Expense added successfully.')

            else:
                print('Failed to add Expense.')


        elif choice == 3:
            user_id = int(input('Enter user_id: '))

            if repo.deleteUser(user_id):
                print('User deleted Successfully.')

            else:
                print('Failed to delete User.')


        elif choice == 4:
            expense_id = int(input('Enter expense_id: '))

            if repo.deleteExpense(expense_id):
                print('Expense deleted Successfully.')

            else:
                print('Failed to delete Expense.')


        elif choice == 5:
            user_id = int(input('Enter user_id: '))

            expenses = repo.getAllExpenses(user_id)

            if expenses:
                for e in expenses:
                    print(f'Expense ID: {e.expense_id}, Amount: {e.amount}, Catrgory ID: {e.category_id}, Date: {e.date}, Description: {e.description}')

            else:
                print('No expense found.')


        elif choice == 6:
            expense_id = int(input('Enter Expense ID: '))
            user_id = int(input('Enter User ID: '))
            amount = Decimal(input('Enter amount: '))
            category_id = int(input('Enter Category ID: '))
            date = input('Enter date(YYYY-MM-DD): ')
            description = input('Enter description: ')

            expense = Expenses(expense_id, user_id, amount, category_id, date, description)

            if repo.updateExpense(user_id,expense):
                print('Expense updated successfully.')

            else:
                print('Failed to update Expense.')


        elif choice == 7:
            print("Exiting application. Goodbye!")
            break


        else:
            print("Invalid choice. Please try again!!!")

if __name__ == "__main__":
    main()
                
                             
                          

