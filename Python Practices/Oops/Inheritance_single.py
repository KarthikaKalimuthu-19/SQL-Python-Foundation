#--single inheritance

class base_person:     #base class
    def display_parent(self):
        print('Base class function')


#deriver class

class derived_child(base_person):
     def display_child(self):
         print('Derived class')


obj=derived_child()
obj.display_parent() #--call base class function
obj.display_child()  #--call derived class function

