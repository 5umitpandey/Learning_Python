def max_usable_chopstick_pairs(N, D, L):
    L.sort()

    usable_pairs = 0

    i = 0
    while i < N - 1:
        if L[i + 1] - L[i] <= D:
            usable_pairs += 1
            i += 2  # Skip the next stick
        else:
            i += 1

    return usable_pairs

N, D = map(int, input().split())
L = [int(input()) for _ in range(N)]

result = max_usable_chopstick_pairs(N, D, L)

print(result)
