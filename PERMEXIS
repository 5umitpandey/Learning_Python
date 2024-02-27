# cook your dish here
t = int(input())

while t:
    n = int(input())
    
    a = []
    a = list(map(int, input().split()))
    
    a.sort()
    
    m = 0
    
    for i in range(n-1):
        if(a[i+1] - a[i] > 1):
            m = 1
            break
        
    if(m == 0):
        print("YES")
    else:
        print("NO")
    t -= 1
