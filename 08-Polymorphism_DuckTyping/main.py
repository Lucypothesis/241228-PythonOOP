# Polymorphism: Greek word that means to 'have many forms or faces'
#               Poly = Many
#               Morphe = Form
# Two ways to achieve polymorphism
# 1. Inheritance: An object could be treated of the same type as a parent class
# 2. 'Duck typing': Object must have necessary attributes/methods
#                   "If it looks like a duck and quacks likea duck, it must be a duck"

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print('WOOF!')

class Cat(Animal):
    def speak(self):
        print('MEOW!')

class Car:
    alive = False # Duck typing: 만약 Car의 alive값이 True라면, Car가 Animal로 취급될 수 있음. 
    def speak(self):
        print('HONK!')

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)

# WOOF!
# True
# MEOW!
# True
# HONK!
# False
