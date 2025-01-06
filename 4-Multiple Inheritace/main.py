# Multiple Inheritance: inherit from more than one parent class
#                       C(A,B)
# Multilevel Inheritance: inherit from a parent which inherits from another parent
#                       C(B) <- B(A) <- A

class Animal:                           # Grandparent # Multilevel Inheritance
    
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating')

    def sleep(self):
        print(f'{self.name} is sleeping')

class Prey(Animal):                     # Parent # Multilevel Inheritance
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):                 # Parent # Multilevel Inheritance
    def hunt(self):
        print(f'{self.name} is hunting')

class Rabbit(Prey):                     # Child # Multilevel Inheritance
    pass

class Hawk(Predator):                   # Child # Multilevel Inheritance
    pass

class Fish(Prey, Predator): # Multiple Inheritance
    pass


rabbit = Rabbit('Bugs')
hawk = Hawk('Tony')
fish = Fish('Nemo')

fish.flee() # Nemo is fleeing
fish.hunt() # Nemo is hunting

rabbit.eat() # Bugs is eating
rabbit.sleep() # Bugs is sleeping