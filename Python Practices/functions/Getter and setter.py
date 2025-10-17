#--Getter and setter task

class Student:
    def __init__(self,marks):
        self.__marks=marks

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks (self,value):
        if value>=0 and value<=100:
            self.__marks=value
        else:
            print('Enter valid marks')

obj=Student(90)
#print(obj.marks)
obj.marks=100
print(obj.marks)
