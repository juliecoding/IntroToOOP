class Shape:
    def __init__(self, name, age):
        self.name = name

    def getArea(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
      self.length = length
      self.width = width

