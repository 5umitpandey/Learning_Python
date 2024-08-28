#1
import math
print(math.sin(0))
print(math.sin(90))

#2
import random
for i in range(5):
    print(random.randrange(10, 50), end = "  " )

import random
seed_value = 0
random.seed(seed_value)
print( random.randint(10, 50))

#3
Temp_in_C = 1
Temp_in_F = Temp_in_C * (9/5) + 32

print("Temp in C = ", Temp_in_C, "\nTemp in F = ", Temp_in_F)

#4
import math
a = 100
b = 80
c = 60

aa = b*b + c*c - 2*b*c* math.cos(a)
bb = a*a + c*c - 2*a*c* math.cos(b)
cc = a*a + b*b - 2*a*b* math.cos(c)

print(aa), print(bb), print(cc)