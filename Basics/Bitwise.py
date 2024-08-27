a = 6   #110
b = 6   #110
c = 4   #100

#AND
print(a&b)  #110
print(a&c)  #100
print('\n')

#OR
print(a|b)  #110
print(a|c)  #110
print('\n')

#XOR
print(a^b)  #000
print(a^c)  #010
print('\n')

#NOT
print(~10)  #1010
print(~100)  #011
print('\n')

#RightShift
print(a >> 1)  #110 >> 1 = 011 = 3
print(c >> 1)  #100 >> 1 = 010 = 2
print('\n')

#LeftShift
print(a << 1)  #0110 << 1 = 1100 = 12
print(c << 1)  #0100 << 1 = 1000 = 8
print('\n')
