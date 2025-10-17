#--abstraction task 2

from abc import *

class Employee(ABC):
    def __init__(self):
        print('Employee salary info')
    def calculate_salary(self,value):
        pass

class Developer(Employee):
    def calculate_salary(self,value):
        return value*1000

class Manager(Employee):
    def calculate_salary(self,value):
        return value*2000

obj1=Developer()
p1=obj1.calculate_salary(3)
print('Developer salary: ',p1)

obj2=Manager()
p2=obj2.calculate_salary(3)
print('Manager salary: ',p2)
