t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    # your code goes here
    p.sort(reverse = True)
    summ = 0
    trig = 0
    count = 0
    
    for i in range(n):
        summ += p[i]
        count += 1
        
        if(summ >= m):
            trig = 1
            break           
            
    if trig == 1:
        print(count)
    else:
        print(-1)
