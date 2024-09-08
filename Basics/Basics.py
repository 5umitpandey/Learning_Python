#NUMERIC

#INT
print(0b1010)    #Binary
print(0o12)      #Octal
print(0xA)       #Hex

#FLOAT
#Maximum value a floating-point: 1.8 ⨉ 10^308
print(1.79e308)     #result 1.79e+308
print(1.8e308)      #result inf

#COMPLEX
print(type(3+6j))       #complex
print( (3+6j).real )    #only real
print( (3+6j).imag )    #only imag
print( (-3+6j).conjugate() )    #conjugate (+ve    --->   -ve)
a=1+2j
b=3+6j
#a*b = (ac-bd) + (ad+bc)
#Complex nums dont support comparasion operators like <, >, <=, >= (TypeError)

#BOOLEAN
a = (3<2)   #Assigning 'True' to a
print(a)


#Precedence
"""
{}      **      ~x, +x, -x      *      /       //     %     +       -       <<, >>    &    ^   | ==,!=,>,>=, <, <=, in, not in     not      and     or
"""

"""
int and float = float
int and complex = complex
float and complex = complex

int(float/num_string)    ->      float/num_string to int     ->      type casting

int(num_string, base)    ->      num_str to int in base      ->      binary/decimal/oct/hex
int("A" / "1010", 2/8)   ->      binary to decimal/octal

complex(int/float)       ->      convert to complex with imaginary part 0
"""

print( int(3.14) )  #3
print( int('3') + int('4') )    #7

print(int('1011', 2))   # convert from binary to decimal int
print(int('341', 8))    # convert from octal to decimal int
print(int('21', 16))    # convert from hex to decimal int

#Data Types
str = "Sumit"                      #String
tup = (1, "Hello", 3)              #Tuple
lst = [1, "Barca", 3]              #List
sett = {1, "Spain", 3, 1, "Spain"} #Set will keep unique items only
dict = {"Name":"Sam", "Age":22}    #Dict

print(str, tup, lst, sett, dict)

#EXPONENT TRICK
print(2**1**3)      #2      -> goes from right to left
print((2**1)**3)    #8



#BITWISE OPERATORS

#10: 1010
# 4: 0100
print( 10 & 4 )     #AND &  1,1 = 1 else 0
print( 10 | 4 )     #OR |   1 = 1,  else 0
print( 10 ^ 4 )     #XOR ^  1,0 = 1 else 0
print( ~10 )        #NOT ~  1010 + 1 = 1011 = -11 (2's Complement)
print( 10 << 2 )    #LEFT SHIFT <<  1010 = 101000 = 40
print( 10 >> 2 )    #RIGHT SHIFT >> 1010 = 10     = 2


#and operations
print(0 and 5)    # Output: 0 (first value is False)
print(5 and 0)    # Output: 0 (second value is False)
print(5 and 10)   # Output: 10 (both values are True, returns the second)
print( 10%(15<10 and 20<30) )   #Error

print(10*4>>2 and 3)    #3
print(5|10&12>>2)       #7

a = 5; a += 10 // 5
print(a)    #7

a = 5; a **= 10 // 5
print(a)

print(10/5-5)   #-3
print(2.5%0.15) #0.10000000000000009

