# class Circle(Shape):
#     def __init__(self, color, is_filled, radius):
#         self.color = color
#         self.is_filled = is_filled
#         self.radius = radius

# class Square(Shape):
#     def __init__(self, color, is_filled, width):
#         self.color = color
#         self.is_filled = is_filled
#         self.width = width

# class Triangle(Shape):
#     def __init__(self, color, is_filled, width, height):
#         self.color = color
#         self.is_filled = is_filled
#         self.width = width
#         self.height = height


# 위와 같이 쓸 거를 class Shape()와 super().__init__(color, is_filled)를 사용해서 아래와 같이 쓸 수 있음


class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
    
    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm^2")
        super().describe() # 부모클래스 describe도 쓰려면 super로 가져와야 함

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width
    
    def describe(self):
        print(f"It is a square with an area of {self.width * self.width}cm^2")
        super().describe() # 부모클래스 describe도 쓰려면 super로 가져와야 함

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"It is a triangle with an area of {self.width * self.height * 0.5}cm^2")
        super().describe() # 부모클래스 describe도 쓰려면 super로 가져와야 함

circle = Circle(color='red', is_filled=True, radius=5)
square = Square(color='red', is_filled=False, width=6)
triangle = Triangle(color='yellow', is_filled=True, width=7, height=8)

print(triangle.color)     # yellow
print(triangle.is_filled) # True
print(triangle.width)     # 7
print(triangle.height)    # 8

circle.describe()   # It is a circle with an area of 78.5cm^2
                    # It is red and filled 
square.describe()   # It is a square with an area of 36cm^2
                    # It is red and not filled
triangle.describe() # It is a traingle with an area of 28.0cm&2
                    # It is yellow and filled