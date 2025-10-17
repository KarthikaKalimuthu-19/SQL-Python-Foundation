#--protected variable : single underscore

class Student:
    def __init__(self,sname,sage):
        self._sname=sname     #--protected variable
        self._age=sage              #-protected variable
        self.__studid=2

    def _disp(self):               #-protected function
        print('Name : ',self._sname,'age : ', self._age)

#--derived class
class Marks(Student):
    def __init__(self,sname,sage,mark1):
        super().__init__(sname,sage)
        self.mark1=mark1   #--public

    def display_studinfo(self):
        print('Name : ',self._sname,'age : ', self._age,'mark : ',self.mark1)


obj=Marks('gracy',21,90)
obj._disp()
obj.display_studinfo()
print(obj._sname)
# print(obj.__studid)  wont access
obj2=Student('raj',2)
#print(obj2.__studid)   wont access private variable outside class


