import re



#tamu = "Texas A&M University"

#tokens = tamu.split(" ") # We split our string on whitespace
#print(len(tokens)) # Prints 3 since we have three components
#print(tokens) # Prints ["Texas", "A&M", "University"]
try:
    file = open("lab_3\shape.txt", "r")
    Shape = file.readline()
    result = re.match("C", Shape)
    print(result) # Prints <_sre.SRE_Match object; span=(0, 1), match='c'>
    result = re.match("R", Shape) # Prints None since "a" is not at the beginning of our string
    print(result)
    file.close()
except IOError:
    print("An error has occurred opening the file.")






#class Circle(Shape):
#    def __init__(self, r):
#        self.r = r
#    def getArea(self):
#        return self.r * self.r * 3.14

#class Triangle(Shape):
#    def __init__(self, b, h):
#        self.b = b
#        self.h = h
#    def getArea(self):
#        return (self.b * self.h) / 2

#class Rectangle(Shape):
#    def __init__(self, l, w):
#        self.l = l
#        self.w = w
#    def getArea(self):
#        return self.l * self.w