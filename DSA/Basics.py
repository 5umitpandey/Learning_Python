#1
print(pow(3,4))

#2
import math
print(math.sqrt(25))

#3
def FindTypeOfTri(a,b,c):

    if( ( a+b <= c ) or ( a+c <= b ) or ( b+c <= a ) ):
        print("This is NOT a Triangle!")
    else:
        print("This is a triangle! This is a: ")
        if(a == b and b == c):
            print("Equ")
        elif(a == b and b != c):
            print("Isosceles")
        else:
            print("Scalane")

a, b, c = map(int,input("Enter 3 numbers: ").split())
FindTypeOfTri(a, b, c)

#4
a, b, c = map(int,input("Enter 3 numbers: ").split())

if( (a^2 + b^2 == c^2) or (b^2 + c^2 == a^2) or (a^2 + c^2 == b^2) ):
    print("Right Angled Triangle")
else:
    print("NOT a Right Angled Triangle")

#5
if( divmod(15, 4)[1] == 0 ):
    print( "It is divisible" )
else:
    print("It is NOT divisible")

#6
list1 = [1, 6, 9, -44, 88, 0, 12, 76, 29, 33]
maxx = max(list1)
minn = min(list1)
print("Max num is: ", maxx)
print("Min num is: ", minn)
print("Max is ", maxx - minn, " values larger")
print("Max is ", maxx / minn, " times larger")

#7: Swapping
#a Using 3rd variable
a = 10
b = 50
print("Before swapping, a = ", a, "b = ", b)

temp = a
a = b
b = temp

print("After swapping, a = ", a, "b = ", b)

#b Using arithmetic operations
a = 99
b = -22
print("Before swapping, a = ", a, "b = ", b)

a = a + b
b = a - b
a = a - b

print("After swapping, a = ", a, "b = ", b)

#c Using swap function
a = 100
b = 444
print("Before swapping, a = ", a, "b = ", b)

a,b = b,a

print("After swapping, a = ", a, "b = ", b)
