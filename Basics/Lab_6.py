#1
l_odd = [1, 3, 5, 7, 9]
l_eve = [2, 4, 6, 8]

l_odd[2] = l_eve # type: ignore

l_flatten = [item for sublist in l_odd for item in (sublist if isinstance(sublist, list) else [sublist])]
# Flattening process: 1 -> [1], 3 -> [3], [2, 4, 6, 8] -> [2, 4, 6, 8], 7 -> [7], 9 -> [9]

l_sort = sorted(l_flatten)

print(l_sort)


#2
import random

l_random = []

for i in range(20):
    i = random.randint(1, 100)
    l_random.append(i)

print(l_random, end = " ")

n = int(input("Enter number to search: "))
if n in l_random:
    print(n, "IS AT:", l_random.index(n) + 1)
else:
    print(n, "IS NOT PRESENT")


#3
l_unique = list(set(l_random))
print(l_unique)


#4
l_words = [ "Red", "Blue", "Orange", "Green", "Black", "White", "Grey"]

l_first_Letter = [word[0] for word in l_words]

print(l_first_Letter)


#5
l_unique = [1, 3, 2, 5, 5, 4]

#mean
mean = sum(l_unique) / len(l_unique)
print("Mean is:", mean)

#median
l_unique = sorted(l_unique)

if( len(l_unique) % 2 == 0 ):
    median = l_unique[ (len(l_unique) + 1) // 2 ]
else:
    median = l_unique[ len(l_unique) // 2 ]
print("Median is:", median)

#mode
mode = max(set(l_unique), key = l_unique.count)
print("Mode is:", mode)

#6
l_tup = [ ("Bread", 30.5), ("Phone", 50000.9), ("Napkin", 0.0) ]

sorted_l_tup = sorted(l_tup, key=lambda x: x[1], reverse=True)

print(sorted_l_tup)


#7
l_tup = [ ((" ", " "), "Bread", 30.5), (), ("Phone", 50000.9), (), ("Napkin", 0.0), () ]

filtered_tuples = [t for t in l_tup if t]

print(filtered_tuples)


#8
l_names = ["Virat", "Dhoni", "Rohit", "Jadeja", "Bumrah"]
l_rolln = [3, 6, 1, 5, 10]
l_marks = [100, 75, 264, 50, 0]

combined_list = list(zip(l_names, l_rolln, l_marks))
print(combined_list)

t_names = tuple(l_names)
t_rolln = tuple(l_rolln)
t_marks = tuple(l_marks)

print(t_names, t_rolln, t_marks, end = "\n")