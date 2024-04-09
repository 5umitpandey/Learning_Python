# cook your dish here
def find_pair_with_difference(arr, B):
    elements = set(arr)
    
    for num in arr:
        if (num + B) in elements or (num - B) in elements:
            return 1  # Pair found
    return 0
    
t = int(input())

while t:
    x,y = map(int, input().split())
    
    a = []
    a = list(map(int, input().split()))
    
    print(find_pair_with_difference(a,y))
    
    t -= 1
