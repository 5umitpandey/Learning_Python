#1
students_marks = { "Alice": [85, 90, 78], "Bob": [92, 88, 84] }

for student, marks in students_marks.items():
    total = sum(marks)
    average = total / len(marks)
    students_marks[student] = [total, average]  

topper = max(students_marks, key=lambda x: students_marks[x][0])
print(f"Topper: {topper}")

for student, marks in students_marks.items():
    print(f"{student}: Total = {marks[0]}, Average = {marks[1]:.2f}")


# Q2
portfolio = {
    'accounts': ['SBI', 'IOB'],
    'shares': ['HDFC', 'ICICI', 'TM', 'TCS'],
    'ornaments': ['10 gm gold', '1 kg silver']
}

portfolio['MF'] = ['Reliance', 'ABSL']

portfolio['accounts'] = ['Axis', 'BOB']

portfolio['shares'].sort()

del portfolio['ornaments']

print(portfolio)



# Q3
prices = {'apple': 50, 'banana': 20, 'milk': 30}
quantities = {'apple': 2, 'banana': 5, 'milk': 1}
total_bill = sum(prices[item] * quantities[item] for item in prices)
print(f"Total bill: {total_bill}")



# Q4
marks = {
    'Subu': {'Maths': 88, 'Eng': 60, 'SSt': 95},
    'Amol': {'Maths': 78, 'Eng': 68, 'SSt': 89},
    'Raka': {'Maths': 56, 'Eng': 66, 'SSt': 77}
}

print(f"Amol's marks in English: {marks['Amol']['Eng']}")

marks['Raka']['Maths'] = 77
sorted_marks = dict(sorted(marks.items()))

print("Sorted dictionary by name:", sorted_marks)



# Q5
interfaces = {
    'eth0': {'IP': '1.1.1.1', 'status': 'up'},
    'eth1': {'IP': '2.2.2.2', 'status': 'up'},
    'wlan0': {'IP': '3.3.3.3', 'status': 'down'},
    'wlan1': {'IP': '4.4.4.4', 'status': 'up'}
}

def find_status(interface):
    return interfaces.get(interface, {}).get('status', 'Not found')

def find_up_interfaces():
    return {iface: data['IP'] for iface, data in interfaces.items() if data['status'] == 'up'}

total_interfaces = len(interfaces)

print(f"Status of eth0: {find_status('eth0')}")
print(f"Interfaces that are up: {find_up_interfaces()}")
print(f"Total interfaces: {total_interfaces}")



# Q6
names_set = set()
names_set.update(['Alice', 'Bob', 'Charlie', 'David', 'Eve'])
names_set.discard('Charlie')
names_set.discard('David')
names_set.add('Frank')



# Q7
import random

random_numbers = {random.randint(15, 45) for _ in range(10)}
count_less_than_30 = sum(1 for num in random_numbers if num < 30)
random_numbers = {num for num in random_numbers if num <= 3}

print(f"Random numbers: {count_less_than_30}")
print(f"Count of numbers less than 30: {count_less_than_30}")



# Q8
def cal_sum_prod(a, b, c):
    return a+b+c, a*b*c

a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
c = int(input("Enter the third integer: "))

sum_result, prod_result = cal_sum_prod(a, b, c)

print(f"Sum: {sum_result}, Product: {prod_result}")



# Q9
def create_tuples():
    return [(x, x**2, x**3) for x in range(1, 21)]

tuples_list = create_tuples()


# Q10
def count_alphabets_digits(s):
    result = {'alphabets': 0, 'digits': 0}
    for char in s:
        if char.isalpha():
            result['alphabets'] += 1
        elif char.isdigit():
            result['digits'] += 1
    return result

sample_string = "Hello123"
print(count_alphabets_digits(sample_string))



# Q11
def count_lower_upper(s):
    result = {'lowercase': 0, 'uppercase': 0}
    for char in s:
        if char.islower():
            result['lowercase'] += 1
        elif char.isupper():
            result['uppercase'] += 1
    return result

sample_string = "HelloWorld"
print(count_lower_upper(sample_string))




# Q12
def compute(n):
    return n + int(f"{n}{n}") + int(f"{n}{n}{n}") + int(f"{n}{n}{n}{n}")

print(compute(4))
print(compute(7))


# Q13
def create_list(list1, list2):
    return list(set(list1) & set(list2))

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print(create_list(list1, list2))



# Q14
def sanitize_list(lst):
    return list(set(lst))

sample_list = [1, 2, 2, 3, 4, 4, 5]
print(sanitize_list(sample_list))