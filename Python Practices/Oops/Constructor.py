#--parameter constructor


class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display_student(self,roll_no):
        print('Name :',self.name)
        print('Age :',self.age)
        print('Roll_no :',roll_no)

obj=Student('abinesh',20)
obj1=Student('vijay',21)

obj.display_student(1)
obj.display_student(2)
        
