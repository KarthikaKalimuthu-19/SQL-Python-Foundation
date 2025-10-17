#--exception for invalid expense ID

class ExpenseNotFoundException(Exception):
    def __init__(self,message='Expense ID not found in the database'):
        super().__init__(message)
