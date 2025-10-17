#sinle inheritance with constructor

class base_person:
    def __init__(self,name):
        self.name=name
        print('Base class constructor')
    def display(self):
        print('Base class function :student name :',self.name)


#deriver class

class derived_child(base_person):
     def add(self,a,b):
         c=a+b
         return c
         


obj=derived_child('abi')
obj.display() #--call base class function
res=obj.add(2,3)
print('Add :',res)
