#1 A string is entered through the keyboard. Write a recursive function that counts the number of vowels in this string.
def count_vowels(s):
    if not s:
        return 0
    return (1 if s[0].lower() in 'aeiou' else 0) + count_vowels(s[1:])

s = input("Enter a string: ")
print("Number of vowels:", count_vowels(s))


#2 Two numbers are received through the keyboard into variables a and b. Write a recursive function that calculate the value of a^b.
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

a = int(input("Enter the base: "))
b = int(input("Enter the exponent: "))
print(f"{a}^{b} =", power(a, b))


#3 Write a recursive function that reverses the list of numbers that it receives. 

def reverse_list(lst):
    if len(lst) == 0:
        return []
    return [lst[-1]] + reverse_list(lst[:-1])


lst = list(map(int, input("Enter numbers separated by space: ").split()))
print("Reversed list:", reverse_list(lst))


#4 A list contains some negative and some positive numbers. Write a recursive function that sanitizes the list by replacing all negative numbers with 0. 

def sanitize_list(lst):
    if not lst:
        return []
    return [0 if lst[0] < 0 else lst[0]] + sanitize_list(lst[1:])

lst = list(map(int, input("Enter numbers separated by space: ").split()))
print("Sanitized list:", sanitize_list(lst))


#5 A string is entered through the keyboard. Write a recursive function that checks whether the string is a palindrome or not.

def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

s = input("Enter a string: ")
print(f"Is the string a palindrome? {is_palindrome(s)}")