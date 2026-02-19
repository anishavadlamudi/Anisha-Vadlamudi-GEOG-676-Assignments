import re

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def getArea(self):
        return self.r * self.r * 3.14

class Triangle(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h
    def getArea(self):
        return (self.b * self.h) / 2

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l 
        self.w = w
    def getArea(self):
         return self.l * self.w


def file_or():
    try:
        file = open("lab_3\shape.txt", "r")
        line = file.readline()
        file.close()

    except IOError:
        print("An error has occurred opening the file.")
    return line


def split_readline(line):
    
    parts = line.split(" ")
    print (len(parts))
    print (parts)
    
    return parts 

def read_parts(parts):

    if parts[0] == "Circle"
       r = parts[1]
       
    elif parts[0] == "Rectangle"
        l = parts[1]
        w = parts[2]
         
    elif  parts[0] == "Triangle"
        b = parts[1]
        h = parts[2]
    
    else
        print "Error in Read_Parts"

def main():

    file_or()
    split_readline()
    read_parts()
    
    
#result = re.match("C", Shape)
#print(result) 
#Prints <_sre.SRE_Match object; span=(0, 1), match='c'>
#    result = re.match("R", Shape) 
#Prints None since "R" is not at the beginning of our string
#   print(result)
