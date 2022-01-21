from math import pi
import math
import sys

class Common:
    def __init__(self, lis1):
        try:
            self.lis1 = lis1
        except:
            return 'Error'
class Triangle(Common):
    def __init__(self, lis1):
        super().__init__(lis1)
        a = lis1[0]; b = lis1[1]; c = lis1[2]
        while(True):
            if a+b <= c or a+c <= b or b+c <= a:
                try:
                    raise ValueError()
                except:
                    print('Exception:\n- Sum of two sides must NOT be lower or equal to the lenght of third side!\nTry Again.')
                    triangle()
            else: break
    def perimeter(hay):
        num = hay.lis1[0]+hay.lis1[1]+hay.lis1[2]
        return num
    def area(self):
        p = (self.lis1[0] + self.lis1[1] + self.lis1[2])/2
        num = (p*(p-self.lis1[0])*(p-self.lis1[1])*(p-self.lis1[2]))**0.5
        return num
class Rectangle(Common):
    def __init__(self, lis1):
        super().__init__(lis1)
    def area(self):
        a = self.lis1[0]; b = self.lis1[1] 
        return a*b
    def perimeter(self):
        a = self.lis1[0]; b = self.lis1[1]
        return 2*(a+b) 
class Square(Common):
    def __init__(self, lis1):
        super().__init__(lis1)
    def area(omg):
        a = omg.lis1[0]
        return a*a
    def perimeter(self):
        a = self.lis1[0]
        return a*4
class Circle(Common):
    def __init__(self, lis1):
        super().__init__(lis1)
    def area(self):
        a = self.lis1[0]
        return a*a*math.pi
    def perimeter(self):
        a = self.lis1[0]
        return 2*a*math.pi
class Polygon(Common):
    def __init__(self, lis1):
        super().__init__(lis1)
    def area(self):
        a = self.lis1[0]; b = self.lis1[1]
        area = (a / (2*(math.tan((math.pi/180)*180/(b))))) * ((a*b)/2)
        return round(area, 2)
    def perimeter(self):
        a = self.lis1[0]; b = self.lis1[1]
        return a*b
class Comparator(Common):
    def __init__(self, lis1):
        super().__init__(lis1)
    def perimeter(self):
        return 2*(self.lis1[0]+self.lis1[1])
    def area(self):
        t = 'sinus'; s = number(t)
        while(True):
            if s > 1 or s <= 0:
                try:
                    raise Exception(ValueError())
                except: 
                    print('Exception:\n- Sinus must be in range (0;1]!\nTry again.')
                    s = number(t)
            elif s == 1: print('It is a rectangle'); break
            else: break
        return self.lis1[0]*self.lis1[1]*s
class Trapeze(Common):
    def __init__(self, lis1):
        super().__init__(lis1)
        a = self.lis1[0]; b = self.lis1[1]; c = self.lis1[2]; d = self.lis1[3]
        while(True):
            if a <= b or a >= b+c+d or c >= a+b+d or d >= a+b+c:
                try:
                    raise ValueError()
                except:
                    print('Exception:\n- Does not exist trapeze with given data!\nTry Again.')
                    trapeze()
            else: break
    def perimeter(s):
        return s.lis1[0] + s.lis1[1] + s.lis1[2] + s.lis1[3]
    def area(s):
        a = s.lis1[0]; b = s.lis1[1]; c = s.lis1[3]; d = s.lis1[3]
        area = math.sqrt((a+c-b+d)*(b+c+d-a)*(a-b-c+d)*(a+c-b-d))*((a+b)/(4*(a-b)))
        return area

def teext(shape):
    print('To stop the opration, enter "back"')
    while(True):
        text = input('Enter what you need: ')
        if text == 'area':
            print(f'The area is: {shape.area()}'); 
        elif text == 'perimeter':
            print(f'The perimeter is: {shape.perimeter()}'); 
        elif text == 'both':
            print(f'The area is: {shape.area()}')
            print(f'The perimeter is: {shape.perimeter()}'); break
        elif text == 'back':
            break
        elif text == 'end':
            sys.exit()
        else:
            print(f'- We do not have data for "{text}".\n- Try again and enter only "area", "perimeter", or "both".')
def number(t):
    while(True):
        n = input(f'Enter {t}: ')
        if n == 'back': 
            begin(); break
        elif n == 'end':
            sys.exit()
        try:
            num = float(n)
            if num < 0:
                raise Exception('Invalid number.')
        except: 
            print('Enter only floating-point or integer numbers bigger than 0!\nTry again.')
        else:
            return num; break
def triangle():
    t = 'side a'; a = number(t)
    t = 'side b'; b = number(t)
    t = 'side c'; c = number(t)
    lis1 = [a,b,c]
    shape = Triangle(lis1)
    teext(shape)
def rectangle():
    t = 'side a'; a = number(t)
    t = 'side b'; b = number(t)
    lis1 = [a,b]
    shape = Rectangle(lis1)
    teext(shape)
def square():
    t = 'side a'; a = number(t)
    lis1 = [a]
    shape = Square(lis1)
    teext(shape)
def circle():
    t = 'radius'; r = number(t)
    lis1 = [r]
    shape = Circle(lis1)
    teext(shape)
def polygon():
    t = 'side a'; a = number(t)
    t = 'number of sides'; n = number(t)
    lis1 = [a,n]
    shape = Polygon(lis1)
    teext(shape)
def comparator():
    t = 'side a'; a = number(t)
    t = 'side b'; b = number(t)
    lis1 = [a,b]
    shape = Comparator(lis1)
    teext(shape)
def trapeze():
    t = 'long base'; a = number(t)
    t = 'short base'; b = number(t)
    t = 'leg'; c = number(t)
    t = 'leg'; d = number(t)
    lis1 = [a,b,c,d]
    shape = Trapeze(lis1)
    teext(shape)
    
def begin():
    print('To stop running the program, enter "end".')
    while(True):
        shape = input('Enter shape you need: ')
        if shape == "triangle":
            triangle()
        elif shape == 'rectangle':
            rectangle()
        elif shape == 'square':
            square()
        elif shape == 'circle':
            circle()
        elif shape == 'polygon':
            polygon()
        elif shape == 'comparator':
            comparator()
        elif shape == 'trapeze':
            trapeze()
        elif shape == 'end' or shape == 'back':
            sys.exit()
        else:
            print('- Shape no founded\nTry again.')
begin()