#1 Suppose a dictionary contains type of pet (cat, dog, etc.), name of pet and age of pet. Write a program that obtains the sum of all dog's ages.
from functools import reduce

pets = [{'type': 'dog', 'name': 'Rex', 'age': 5}, {'type': 'cat', 'name': 'Whiskers', 'age': 3}, {'type': 'dog', 'name': 'Buddy', 'age': 7}]
dog_ages = map(lambda pet: pet['age'], filter(lambda pet: pet['type'] == 'dog', pets))
sum_dog_ages = reduce(lambda a, b: a + b, dog_ages)
print(sum_dog_ages)


#2 Consider the following list:
# lst = [1.25, 3.22, 4.68, 10.95, 32.55, 12.54] 
# The numbers in the list represent radii of circles. Write a program to obtain a list of areas of these circles rounded off to two decimal places.
import math

radii = [1.25, 3.22, 4.68, 10.95, 32.55, 12.54]
areas = list(map(lambda r: round(math.pi * r**2, 2), radii))
print(areas)


#3 Consider the following lists:
# nums = [10, 20, 30, 40, 50, 60, 70, 80]
# strs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
# Write a program to obtain a list of tuples, where each tuple contains a number from one list and a string from another, in the same order in which they appear in the original lists.
nums = [10, 20, 30, 40, 50, 60, 70, 80]
strs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
tuples_list = list(map(lambda x, y: (x, y), nums, strs))
print(tuples_list)


#4 Suppose a dictionary contains names of students and marks obtained by them in an examination.
# Write a program to obtain a list of students who obtained more than 40 marks in the examination. 
students = {'Alice': 35, 'Bob': 55, 'Charlie': 42, 'Dave': 30}
passed_students = list(filter(lambda name: students[name] > 40, students))
print(passed_students)


#5 Consider the following list:
# lst = ['Malayalam', 'Drawing', 'madamIamadam', '1234321']
# Write a program to print those strings which are palindromes
lst = ['Malayalam', 'Drawing', 'madamIamadam', '1234321']
palindromes = list(filter(lambda s: s.lower() == s[::-1].lower(), lst))
print(palindromes)


#6. A list contains names of employees. Write a program to filter out those names whose length is more than 8 characters
employees = ['Alexander', 'Bob', 'Christine', 'David', 'Elizabeth']
long_names = list(filter(lambda name: len(name) > 8, employees))
print(long_names)


#7. A dictionary contains following information about 5 employees: First name, Last name, Age, Grade (Skilled, Semi-skilled, Highly-skilled).
# Write a program to obtain a list of employees (first name + last name) who are Highly-skilled.
employees = [
    {'first_name': 'John', 'last_name': 'Doe', 'age': 28, 'grade': 'Highly-skilled'},
    {'first_name': 'Jane', 'last_name': 'Smith', 'age': 34, 'grade': 'Skilled'},
    {'first_name': 'Emily', 'last_name': 'Davis', 'age': 22, 'grade': 'Highly-skilled'},
    {'first_name': 'Chris', 'last_name': 'Brown', 'age': 31, 'grade': 'Semi-skilled'},
    {'first_name': 'Katie', 'last_name': 'Johnson', 'age': 27, 'grade': 'Highly-skilled'}
]

highly_skilled = list(map(lambda emp: f"{emp['first_name']} {emp['last_name']}", filter(lambda emp: emp['grade'] == 'Highly-skilled', employees)))
print(highly_skilled)