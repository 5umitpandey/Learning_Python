# cook your dish here
def remove_duplicates(nums):
    if not nums:
        return 0

    i = 0

    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    # Print the new length of the list
    print(i + 1)

    # Print the elements of the list
    for k in range(i + 1):
        print(nums[k], end=' ')
    print()

    return i + 1
    
t = int(input())

while t:
    n = int(input())
    
    a = []
    a = list(map(int, input().split()))
    
    remove_duplicates(a)
    
    t -= 1
