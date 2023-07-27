from abc import ABC, abstractmethod


class Shape(ABC):
    # 추상메서드
    @abstractmethod
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    # 생성자
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # return self.radius * self.radius * 3.14
        return pow(self.radius, 2) * 3.14

    def perimeter(self):
        return 2 * 3.14 * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


circle = Circle(10)
print('원 넓이: {0}'.format(circle.area()))  # 원 넓이: 314.0
print('원 둘레: {0}'.format(circle.perimeter()))  # 원 둘레: 62.800000000000004

rectangle = Rectangle(4, 6)
print('사각형 넓이: {0}'.format(rectangle.area()))  # 사각형 넓이: 24
print('사각형 둘레: {0}'.format(rectangle.perimeter()))  # 사각형 둘레: 20
