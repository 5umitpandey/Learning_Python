n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    if i % 2 == 0:
        print(*a[i])
    else:
        print(*reversed(a[i]))
