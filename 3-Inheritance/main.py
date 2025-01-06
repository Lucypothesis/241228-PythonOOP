# Inheritance: Allows a class to inherit attributes and methods from another class
#              Helps with code reusability and extensibility
#              class Child(Parent)

class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True
    
    def eat(self):
        print(f'{self.name} is eating')

    def sleep(self):
        print(f'{self.name} is sleeping')

class Dog(Animal): # Inheritance
    # def __init__(self,name):
    #     self.name = name
    #     self.is_alive = True
    
    # def eat(self):
    #     print(f'{self.name} is eating')

    # def sleep(self):
    #     print(f'{self.name} is sleeping')
    pass # 위 내용들을 다 생략하고 pass로 쓸 수 있음

class Cat(Animal): 
    pass

class Mouse(Animal):
    def speak(self):
        print('SQUEEK!')

dog = Dog('Scooby')
cat = Cat('Garfield')
mouse = Mouse('Micky')

print(mouse.name)     # Micky
print(mouse.is_alive) # True
mouse.eat()           # Micky is eating
mouse.sleep()         # Micky is sleeping
mouse.speak()         # SQUEEEK!