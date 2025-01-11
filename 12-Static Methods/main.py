class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def get_info(self):
        return f'{self.name} = {self.position}'
    
    @staticmethod # don't need to rely on any objects to use this method
    def is_valid_position(position): # self 안 들어감
        valid_positions = ['Manager', 'Cashier', 'Cook', 'Janitor']
        return position in valid_positions


# Non Static Methods
employee1 = Employee('Eugene', 'Manager')
employee2 = Employee('Squidward', 'Cashier')
employee3 = Employee('Spongebob', 'Cook')

print(employee1.get_info()) # Eugene = Manager
print(employee2.get_info()) # Squidward = Cashier
print(employee3.get_info()) # Spongebob = Cook


# Static Methods
print(Employee.is_valid_position('Cook')) # True
print(Employee.is_valid_position('Rocket Scientist')) # False