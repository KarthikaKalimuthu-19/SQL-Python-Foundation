#--Expenses entity

class Expenses:
    def __init__(self, expense_id, user_id, amount, category_id, date, description):
       self.expense_id = expense_id
       self.user_id = user_id
       self.amount = amount
       self.category_id = category_id
       self.date = date
       self.description = description
