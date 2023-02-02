# Object-Oriented Programming (OOP)

# Everything in OOP is an object and objects are modelled against real world objects.

# Classes are the templates we use to create objects
# Classes are a way of bringing both data and functionality of our code together.

# Create a class

class Dog:

    animal_kind = "Canine" # class variable


    def bark(self): # method
        return "woof"

# self - "I'm referring to the current class.

# print(Dog.animal_kind)
# print(Dog.bark()) # ERROR

# Instantiation of a class

fido = Dog()
lassie = Dog()

print(type(fido))
print(type(lassie))
print(fido.animal_kind)
print(lassie.animal_kind)
print(fido.bark())

# fido.animal_kind = "Dolphin"
# lassie.animal_kind = "Monkey"

# lassie.animal_kind = "Turtle"
Dog.animal_kind = "Dolphin"  # Instance variable

print(fido.animal_kind) # Now outputs Dolphin
print(lassie.animal_kind) # Now outputs Dolphin

# The Dog's can still access their method
print(fido.bark())
print(lassie.bark())
