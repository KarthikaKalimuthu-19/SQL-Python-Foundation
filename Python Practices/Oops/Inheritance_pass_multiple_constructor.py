#Single inheritance with more constructors

class base_person:
    def __init__(self,name):
        self.name=name
        print('Base class constructor')
    def display(self):
        print('Base class function :student name :',self.name)


#deriver class

class derived_child(base_person):
    def __init__(self,name,emp_salary,emp_id):
     super().__init__(name)
     self.salary=emp_salary
     self.ID=emp_id
    
    def add(self,a,b):
        c=a+b
        return c

    def display_empinfo(self):
        print('Name :',self.name,'ID :',self.ID,'Salary :',self.salary)
         


obj=derived_child('abi',1,20000)
obj.display() #--call base class function
res=obj.add(2,3)
print('Add :',res)
obj.display_empinfo()
