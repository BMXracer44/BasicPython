#Alex Ferguson

from helper import get_int

#A class is a blueprint for an object

# class Person: 
# #Property is a variable stored inside of an object
# name = "Alex"

# #create a new object we run an initialization method (thats whyt it looks like a function call)
# #Person one and two are instances of the person object
# person_one = Person()
# person_two = Person()

# #When we mutate a property it is called a setter
# person_two.name = "Alex"

# #The period is the member operator
# #When we access a property it is called a getter
# print(person_one.name)
# print(person_two.name)

class Person:
    #Self refers to the current instance of the object
    #included an initialization method that sets up the members of the object
    # members are properties (variable) and methos (function)
    def __init__(self, name, age):
        self.name = name
        self.age = age
 

person_one = Person("Alex", 18)
person_two = Person("Patrick", 42)

print(person_one.name + ", " + str(person_one.age))
print(person_two.name + ", " + str(person_two.age))


person_three = Person(input("Enter name: "), get_int("Age: "))

print(person_three.name + ", " + str(person_three.age))

