#--With multiple variables

class Employee:
    def __init__(self,name,salary,position):
        self.name=name
        self.salary=salary
        self.position=position

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        if value!='':
            self.__name=value
        else:
            print('Name should not be empty')
            self.__name=None

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,value):
        if value>5000:
            self.__salary=value
        else:
            print('Salary should be greater than 5000')
            self.__salary=None

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self,value):
        if value=='Manager' or value=='Developer':
            self.__position=value
        else:
            print('Position should be either Manager or Developer')
            self.__position=None


obj=Employee('Karthika',20000,'Manager')
print('Name :',obj.name,'\nSalary :',obj.salary,'\nPosition :',obj.position)
print('\n')
sal=obj.salary=25000
print('updated salary :',sal)
print('\n')
obj1=Employee('Karthika',30000,'Developer')
print('Name :',obj1.name,'\nSalary :',obj1.salary,'\nPosition :',obj1.position)


    
    
