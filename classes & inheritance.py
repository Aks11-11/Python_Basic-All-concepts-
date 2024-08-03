#define
class MyNewClass:
    pass

# Class Instantiation
my = MyNewClass()

#constructors
class Animal:
    def __init__(self, voice):
        self.voice = voice


cat = Animal('Meow')
print(cat.voice)  # => Meow

dog = Animal('Woof')
print(dog.voice)  # => Woof

#Mehtod
class Dog:

    # Method of the class
    def bark(self):
        print("Ham-Ham")


charlie = Dog()
charlie.bark()  # => "Ham-Ham"

#class variables
class MyClass:
    class_variable = "A class variable!"


# => A class variable!
print(MyClass.class_variable)

x = MyClass()

# => A class variable!
print(x.class_variable)

#super() function

class ParentClass:
    def print_test(self):
        print("Parent Method")


class ChildClass(ParentClass):
    def print_test(self):
        print("Child Method")
        # Calls the parent's print_test()
        super().print_test()

#repr() method
class Employee:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


john = Employee('John')
print(john)  # => John

#polymorphism
class ParentClass:
    def print_self(self):
        print('A')


class ChildClass(ParentClass):
    def print_self(self):
        print('B')


obj_A = ParentClass()
obj_B = ChildClass()

obj_A.print_self()  # => A
obj_B.print_self()  # => B

#overriding

class ParentClass:
    def print_self(self):
        print("Parent")


class ChildClass(ParentClass):
    def print_self(self):
        print("Child")


child_instance = ChildClass()
child_instance.print_self()  # => Child

#inheritance
class Animal:
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs


class Dog(Animal):
    def sound(self):
        print("Woof!")


Yoki = Dog("Yoki", 4)
print(Yoki.name)  # => YOKI
print(Yoki.legs)  # => 4
Yoki.sound()  # => Woof!

#user-defined-expectations
class CustomError(Exception):
    pass

