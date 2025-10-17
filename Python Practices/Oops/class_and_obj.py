#class and object

class one:
    company_name='hexaware'
    
    def fun1(self):
        a=10
        print('Function 1 is called')
        print('A =',a)

    def fun2(self,location):
        print('Location :',location)
        


#object

obj1=one()  #--create the object
obj1.fun1()  #--calling the function with the object

obj2=one()
obj2.fun1()

print(obj1.company_name)
print(one.company_name)

obj1.fun2('chennai')
obj2.fun2('bangalore')
