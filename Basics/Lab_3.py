#1
length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))

area = length * breadth
permimeter = 2 * (length + breadth)

print("\nArea is: ", area)
print("Perimeter is: ", permimeter)

if( area > permimeter ):
    print("\nArea is larger!")
else:
    print("\nPerimeter is larger!")


#2
x1, y1 = 5 , 3
x2, y2 = 15 , 3
x3, y3 = 25 , 4

A = 0.5 * abs( x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2) )

if( A == 0 ):
    print("Points lie on one straight line")
else:
    print("Points DO NOT lie on one straight line")


#3
import math
h,k = 0, 0
r = 4

x,y = map(int, input("Enter two numbers as x,y: ").split())

d = math.sqrt( ((x-h)**2) + ((y-k)**2) )

if( d < r ):
    print("Point is INSIDE")
elif( d == r ):
    print("Point is ON the CIRCLE")
elif( d > r ):
    print("Point is OUTSIDE")


#4
x,y = map(int, input("Enter two numbers as x,y: ").split())

if( (x==0) and (y==0) ):
    print("Point is on ORIGIN")
elif( (x==0) and (y!=0) ):
    print("Point is on Y-Axis")
elif( (x!=0) and (y==0) ):
    print("Point is on X-Axis")
else:
    print("Point is NEITHER on X NOR y")


#5
year = int(input("Enter year: "))

# if( year % 4 == 0 ):
#     if( year % 100 == 0 ):
#         if( year % 400 == 0 ):
#             print("LEAP YEAR")
#         else:
#             print("NOT LEAP YEAR")
#     else:
#         print("LEAP YEAR")
# else:
#     print("NOT LEAP YEAR")

if( (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0) ):
    print("LEAP YEAR")
else:
    print("NOT LEAP YEAR")