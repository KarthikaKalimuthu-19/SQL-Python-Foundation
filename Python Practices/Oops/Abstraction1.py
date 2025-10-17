#--abstract class task 2

from abc import *

class Vehicle(ABC):
    def fuel_type(self):    #--if we are giving one parameter in the abs class then derived methods also should have one parameter.
        pass

class Car(Vehicle):
    def fuel_type(self):    #--ifwe want to pass more value then we should pass it in abs class must.
        return 'Petrol'

class Bike(Vehicle):
    def fuel_type(self):
        return 'Electric'

class Truck(Vehicle):
    def fuel_type(self):
        return 'Diesel'

obj1=Car()
car=obj1.fuel_type()
obj2=Bike()
bike=obj2.fuel_type()
obj3=Truck()
truck=obj3.fuel_type()

print('Car runs on: ',car,'\nBike runs on: ',bike,'\nTruck runs on: ',truck)

        
