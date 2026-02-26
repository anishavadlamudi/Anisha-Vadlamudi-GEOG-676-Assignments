import re
#create classes 
class Shape():
    def __init__(self):
        pass

class Rectangle(Shape):
    def __init__(self, l, w):        
        self.length = l
        self.width = w
    def getArea(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, r):
        self.radius = r
    def getArea(self):
        return 3.14 * self.radius ** 2

class Triangle(Shape):
    def __init__(self, b, h):
        self.base = b
        self.height = h
    def getArea(self):
        return 0.5 * self.base * self.height
    
# read txt file
file = open(r'C:\Users\Anish\Documents\GitHub\Anisha-Vadlamudi-GEOG-676-Assignments\lab_3\shape.txt', 'r')   
lines = file.readlines()
file.close()

for line in lines:
    values = line.strip().split(',')
    shape = values[0]
    if shape == 'Rectangle':
        rect = Rectangle(int(values[1]), int(values[2]))
        print('Area of Rectangle: ', rect.getArea())
    elif shape == 'Circle':
        circ = Circle(int(values[1]))
        print('Area of Circle: ', circ.getArea())
    elif shape == 'Triangle':
        tri = Triangle(int(values[1]), int(values[2]))
        print('Area of Triangle is: ', tri.getArea())
    else:
        pass 