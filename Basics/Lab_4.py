#1
nums = [1, 2, 3]
for i in (nums):
    for j in(nums):
        for k in (nums):
            if( i!=j and j!=k and i!=k ):
                print(i,j,k)
print("\n")

#2
import string

for char in (string.ascii_lowercase):
    print(char, end = " ")
print("\n")
for char in (string.ascii_uppercase):
    print(char, end = " ")

#3
lst = ['desert', 'dessert', 'to', 'too', 'lose', 'loose'] 
s = 'Mumbai'
i = 0
# while i < len(lst) :
#     if i > 3 :
#         break
#     else :
#         print(i, lst[i], s[i])
#         i += 1
for i in range(4):
    print(i, lst[i], s[i])

#4
n = int(int(input("Enter a 5 digit number: ")))

rev_num = 0
while n > 0:
    remainder = n % 10
    rev_num = rev_num * 10 + remainder
    n = n // 10

print("Reversed num is: ", rev_num)

if( rev_num == n ):
    print("\nBoth are SAME")
else:
    print("\nBoth are DIFFERENT")

#5
for i in range(1, 501, 1):
    num = originalNum = remainder = n = result = 0
    originalNum = i

    #store the number of digits of i in n
    while (originalNum != 0):
        originalNum //= 10
        n += 1

    originalNum = i

    while (originalNum != 0):
        remainder = originalNum % 10

        #calculate remainder^n
        power = 1
        for _ in range(n):
            power *= remainder

        result += power
        originalNum //= 10

    #if i is equal to result, the number is an Armstrong number
    if (result == i):
        print(i, end=" ")
     