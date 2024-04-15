def max_sum_of_k_elements(nums, k):
    
    max_sum = sum(nums[:k])
    current_sum = max_sum
    
    # Slide the window of 'k' elements and find the maximum sum
    for i in range(len(nums) - k):
        current_sum = current_sum - nums[i] + nums[i + k]
        max_sum = max(max_sum, current_sum)
    
    return max_sum
    
# cook your dish here
t = int(input())

while t:
    x,y = map(int, input().split())
    
    a = []
    a = list(map(int, input().split()))
    
    print(max_sum_of_k_elements(a, y))
    
    t -= 1
