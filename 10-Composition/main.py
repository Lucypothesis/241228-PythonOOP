# Composition

class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

class Wheel:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(horse_power)                     # Composition
        self.wheels = [Wheel(wheel_size)for wheel in range(4)] # Composition
    
    def display_car(self):
        return f"{self.make} {self.model} {self.engine.horse_power} {self.wheels[0].size}"

# Composition이라 Engine()과 Wheel()을 밖에다 쓰지 않고 안에 씀
# class Car는 Engine과 4개의 Wheel을 'Own'하고 있음
# 이 점이 aggregation과 다른 점임. Aggregation은 'Has-a' 관계임

car1 = Car(make="Ford", model="Mustang", horse_power=500, wheel_size=18)
car2 = Car(make="Chevrolet", model="Corvette", horse_power=670, wheel_size=19)

print(car1.display_car())
print(car2.display_car())