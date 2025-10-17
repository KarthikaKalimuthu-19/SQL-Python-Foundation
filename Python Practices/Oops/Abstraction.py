#--abstract class tasks

from abc import *

class Animal(ABC):
    def make_sound():
        pass

class Dog(Animal):
    def make_sound(self):
        print('Dog says: Woof!')

class Cat(Animal):
    def make_sound(self):
        print('Cat says: Meow!')

obj=Dog()
obj1=Cat()
obj.make_sound()
obj1.make_sound()
