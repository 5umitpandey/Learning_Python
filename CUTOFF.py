t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    # your code goes here
    #A[X-1]-1
    a.sort(reverse=True)
    #print(a)
    print(a[x-1] - 1)
