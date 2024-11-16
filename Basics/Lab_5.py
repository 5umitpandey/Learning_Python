#1
p, r, q, n = map(int, input("Enter values of p, r, q, n: ").split())

a = p * ( 1 + r / q ) ** n * q

print(a)


#2
def Pythagorean_Triplet(n):
    triplets = []

    for a in range(1, n+1):
        for b in range(a, n+1):
            c = (a**2 + b**2) ** 0.5
            if c.is_integer() and c <= n:
                triplets.append( (a, b, int(c)) )
    
    return triplets

for triplet in Pythagorean_Triplet(30):
    print(triplet)


#3
population = 100000
rate = 10
years = 10

year = 0
for year in range(years):
    population += (population * rate) // 100
    print("Population after", year+1, "year is:" , population)


#4
# def find_ramanujan_numbers(limit):
#     ramanujan_numbers = []
#     for a in range(1, limit):
#         for b in range(a, limit):
#             for c in range(1, limit):
#                 for d in range(c, limit):
#                     if a**3 + b**3 == c**3 + d**3 and a != c and a != d:
#                         ramanujan_numbers.append((a, b, c, d, a**3 + b**3))
#     return ramanujan_numbers

# limit = 20
# ramanujan_numbers = find_ramanujan_numbers(limit)
# for numbers in ramanujan_numbers:
#     print(f"{numbers[4]} = {numbers[0]}^3 + {numbers[1]}^3 = {numbers[2]}^3 + {numbers[3]}^3")


def ram(n):
    for i in range(1, n):
        count = 0
        for j in range(1, 100):
            for k in range(j, 100):
                if( j**3 + k**3 ) == i:
                    count += 1
        if count == 2:
            print(i)
ram(4200)

#5
for i in range(1,25):
    if( i < 12 ):
        print("Time is:", i, " AM")
    elif( i == 12 ):
        print("Time is:", i, "Noon")
    elif( i > 12 and i < 24 ):
        print("Time is:", i, " PM")
    else:
        print("Time is:", i, " MIDNIGHT")