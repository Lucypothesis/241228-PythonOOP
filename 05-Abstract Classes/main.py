# ABC: Abstract Base Class
#      abstract class의 부모클래스 역할을 함
#      인스턴스를 생성하지 못하게 제한함
# abstractmethod: 자식클래스에 꼭 들어가야 하는 메서드 정의함
from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod # 자식클래스에 꼭 들어가야 함
    def go(self): 
        pass

    @abstractmethod # 자식클래스에 꼭 들어가야 함
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print('You drive the car')

    def stop(self):
        print('You stop the car')

car = Car()

car.go() # You drive the car
car.stop() # You stop the car


class Motorcycle(Vehicle):
    def go(self):
        print('You ride the motorcycle')

    def stop(self):
        print('You stop the motorcycle')

motorcycle = Motorcycle()

motorcycle.go() # You ride the motorcycle
motorcycle.stop() # You stop the motorcycle


class Boat(Vehicle):
    def go(self):
        print('You sail the boat')
    def stop(self):
        print('You anchor the boat')

boat = Boat()

boat.go() # You sail the boat
boat.stop() # You anchor the boat
