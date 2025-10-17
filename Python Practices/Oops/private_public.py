#--private double underscore, public is default

class bank:
    def __init__(self,accno,name):
        self.__accno=accno    #---private variable
        self.name=name       #--public variable

    def display(self):
        print('Accno : ',self.__accno,'Name : ',self.name)

    def   __displayinfo(self):      #---private function
        print('Accno : ' ,self.__accno)


obj=bank(101,'sachita')
obj.display()

# print( obj.__accno)   cant access private variable outside class
print(obj.name)

obj.__displayinfo()
        
