def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_prime(a,b):
    count = 0
    for num in range(a, b+1):
        if is_prime(num):
            print(num, end=" ")
            count += 1
            if count == 100:
                break
a = 100
b = 200
print_prime(a,b)