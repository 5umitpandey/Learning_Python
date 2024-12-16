#1
# Write a program to create a class that represents Complex numbers containing real and imaginary parts
# and then use it to perform complex number addition, subtraction, multiplication as well as complex conjugate.
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def add(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def subtract(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def multiply(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return Complex(real_part, imag_part)

    def conjugate(self):
        return Complex(self.real, -self.imag)

    def display(self):
        print(f"{self.real} + {self.imag}i")


a = Complex(4, 3)
b = Complex(6, 2)

c = a.add(b)
print("Addition:")
c.display()

d = a.subtract(b)
print("Subtraction:")
d.display()

e = a.multiply(b)
print("Multiplication:")
e.display()

f = a.conjugate()
print("Conjugate of a:")
f.display()



#2 Write a program to create a class that can calculate the surface area and volume of a solid. The class should also have a provision to accept the data relevant to the solid.
import math

class Sphere:
    def __init__(self, radius=0):
        self.radius = radius

    def set_data(self, radius):
        self.radius = radius

    def surface_area(self):
        # 4πr^2
        return 4 * math.pi * self.radius**2

    def volume(self):
        # (4/3)πr^3
        return (4/3) * math.pi * self.radius**3

    def display(self):
        print(f"Radius: {self.radius}")
        print(f"Surface Area: {self.surface_area():.2f}")
        print(f"Volume: {self.volume():.2f}")

sphere = Sphere()
sphere.set_data(5)
sphere.display()


#3
# Write a program to create a class that can calculate the perimeter / circumference and area of a regular shape. 
# The class should also have a provision to accept the data relevant to the shape.
import math

class Shape:
    def __init__(self, side=None, radius=None, length=None, width=None, base=None, height=None):
        self.side = side
        self.radius = radius
        self.length = length
        self.width = width
        self.base = base
        self.height = height

    def square_perimeter(self):
        if self.side is not None:
            return 4 * self.side

    def square_area(self):
        if self.side is not None:
            return self.side ** 2

    def circle_circumference(self):
        if self.radius is not None:
            return 2 * math.pi * self.radius

    def circle_area(self):
        if self.radius is not None:
            return math.pi * self.radius ** 2

    def rectangle_perimeter(self):
        if self.length is not None and self.width is not None:
            return 2 * (self.length + self.width)

    def rectangle_area(self):
        if self.length is not None and self.width is not None:
            return self.length * self.width

    def triangle_perimeter(self):
        if self.side is not None:
            return 3 * self.side

    def triangle_area(self):
        if self.base is not None and self.height is not None:
            return 0.5 * self.base * self.height

# Square
square = Shape(side=4)
print("Square Perimeter:", square.square_perimeter())
print("Square Area:", square.square_area())

# Circle
circle = Shape(radius=5)
print("Circle Circumference:", circle.circle_circumference())
print("Circle Area:", circle.circle_area())

# Rectangle
rectangle = Shape(length=4, width=5)
print("Rectangle Perimeter:", rectangle.rectangle_perimeter())
print("Rectangle Area:", rectangle.rectangle_area())

# Triangle
triangle = Shape(side=3, base=4, height=5)
print("Triangle Perimeter:", triangle.triangle_perimeter())
print("Triangle Area:", triangle.triangle_area())



#4
# If a class D is derived from two base classes B1 and B2, then write these classes each containing a constructor.
# Ensure that while building an object of type D, constructor of B2 should get called. Also provide a destructor in each class.
# In what order would these destructors get called?
class B1:
    def __init__(self):
        print("Constructor of B1")

    def __del__(self):
        print("Destructor of B1")


class B2:
    def __init__(self):
        print("Constructor of B2")

    def __del__(self):
        print("Destructor of B2")


class D(B2, B1):
    def __init__(self):
        super().__init__()
        print("Constructor of D")

    def __del__(self):
        print("Destructor of D")


obj = D()
del obj



#5
# Suppose there is a base class B and a derived class D derived from B. B has two public member functions b1( ) and b2( ), whereas D has two member functions d1( ) and d2( ). 
# Write these classes for the following different situations: should be accessible from main module, b2( ) should not be. b1( ) Neither b1( ), nor b2( ) should be accessible from main module accessible from main module. Both b1( ) and b2( ) should be accessible from main module.

class Base1:
    def b1(self):
        print("Public method b1 from class Base1")
    
    def __b2(self):  # Private method
        print("Private method b2 from class Base1")

class Derived1(Base1):
    def d1(self):
        print("Public method d1 from class Derived1")
    
    def d2(self):
        print("Public method d2 from class Derived1")

# Main module
b_obj1 = Base1()
b_obj1.b1()  # Accessible
# b_obj1.__b2()  # Not accessible (private method)

d_obj1 = Derived1()
d_obj1.d1()  # Accessible
d_obj1.d2()  # Accessible
d_obj1.b1()  # Accessible
# d_obj1.__b2()  # Not accessible (private method)



class B:
    def __b1(self):  # Private method
        print("Private method b1 from class B")
    
    def __b2(self):  # Private method
        print("Private method b2 from class B")

class D(B):
    def d1(self):
        print("Public method d1 from class D")
    
    def d2(self):
        print("Public method d2 from class D")

# Main module
b_obj = B()
# b_obj.__b1()  # Not accessible (private method)
# b_obj.__b2()  # Not accessible (private method)

d_obj = D()
d_obj.d1()  # Accessible
d_obj.d2()  # Accessible
# d_obj.__b1()  # Not accessible (private method)
# d_obj.__b2()  # Not accessible (private method)



class B:
    def b1(self):
        print("Public method b1 from class B")
    
    def b2(self):
        print("Public method b2 from class B")

class D(B):
    def d1(self):
        print("Public method d1 from class D")
    
    def d2(self):
        print("Public method d2 from class D")

# Main module
b_obj = B()
b_obj.b1()  # Accessible
b_obj.b2()  # Accessible

d_obj = D()
d_obj.d1()  # Accessible
d_obj.d2()  # Accessible
d_obj.b1()  # Accessible
d_obj.b2()  # Accessible
