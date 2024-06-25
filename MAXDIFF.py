# cook your dish here
t = int(input())

while t:
    n,k = map(int, input().split())
    
    y = list(map(int,input().split()))
    y.sort()
    
    if( k > n // 2 ):
        s1 = sum( y[:n - k] )
        s2 = sum( y[n - k:] )
    else:
        s1 = sum( y[:k] )
        s2 = sum( y[k:] )
        
    print(abs(s2 - s1))
    
    t -= 1
