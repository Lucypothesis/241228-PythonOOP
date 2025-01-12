# Property Decorater: Decorator used to define a method as a property
#                     It can be accessed like an attribute
#                     Benefit: Add additional logic when read, write or delete attributes
#                     Gives getter, setter, and deleter method

class Rectangle:
    def __init__(self, width, height):
        self._width = width   # _width: private attribute, 클래스 내부에서만 사용
        self._height = height # _height: private attribute, 클래스 내부에서만 사용

    @property # Property Decorater를 통해 Attribute 처럼 접근될 수 있음
    def width(self):
        return f'{self._width: .1f}cm'

    @property # Property Decorater를 통해 Attribute 처럼 접근될 수 있음
    def height(self):
        return f'{self._height: .1f}cm'
    
    @width.setter # setter method
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print('Width must be greater than zero')

    @height.setter # setter method
    def height(self, new_heigth):
        if new_heigth > 0:
            self._height = new_heigth
        else:
            print('Height must be greater than zero')

    @width.deleter # deleter method
    def width(self):
        del self._width
        print('Width has been deleted')

    @height.deleter # deleter method
    def height(self):
        del self._height
        print('Height has been deleted')


rectangle = Rectangle(3,4)


print(rectangle._width)  # 3
print(rectangle._height) # 4

# Property Decorater를 통해 Attribute 처럼 접근될 수 있음
rectangle.width = 5
rectangle.height = 6

print(rectangle._width)  # 5
print(rectangle._height) # 6

del rectangle.width      # Width has been deleted
del rectangle.height     # Height has been deleted