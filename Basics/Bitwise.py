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


#10: 1010
# 4: 0100
print( 10 & 4 )     #AND &  1,1 = 1 else 0
print( 10 | 4 )     #OR |   1 = 1,  else 0
print( 10 ^ 4 )     #XOR ^  1,0 = 1 else 0
print( ~10 )        #NOT ~  1010 + 1 = 1011 = -11 (2's Complement)
print( 10 << 2 )    #LEFT SHIFT <<  1010 = 101000 = 40
print( 10 >> 2 )    #RIGHT SHIFT >> 1010 = 10     = 2
