t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    
    s.sort()
    
    i = 0
    x = s[i+1] - s[i]
    
    for i in range(n-1):
        if(((s[i+1] - s[i])) < x):
            x = s[i+1] - s[i]
    
    print(x)
