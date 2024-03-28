# cook your dish here
t = int(input())

while t:
    x,y,z = map(int, input().split())
    
    a = sorted(list(map(int, input().split())))[::-1]
    b = sorted(list(map(int, input().split())))[::-1]
    
    ans = 0
    
    for i in range(min(x, y)):
        ans += min(a[i], z*b[i])
        
    print(ans)
    
    t -= 1
