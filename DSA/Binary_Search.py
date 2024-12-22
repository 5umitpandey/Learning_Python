def recursive_binary_search(arr, target, left, right):
    if left > right:
        return -1
    
    mid = left + (right - left) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return recursive_binary_search(arr, target, left, mid - 1)
    else:
        return recursive_binary_search(arr, target, mid + 1, right)

arr = [2, 3, 4, 10, 40]
target1 = 10
target2 = 20

result1 = recursive_binary_search(arr, target1, 0, len(arr) - 1)
result2 = recursive_binary_search(arr, target2, 0, len(arr) - 1)

print(result1)
print(result2)
