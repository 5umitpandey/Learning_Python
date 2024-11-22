#https://www.geeksforgeeks.org/problems/reverse-array-in-groups0255/1?page=1&difficulty=School,Basic&sortBy=submissions

def reverseInGroups(self, arr, k):
        n = len(arr)
        for i in range (0, n, k):
            left = i
            right = min(i + k - 1, n - 1)
            #Reverse the subarray from left to right
            while(left < right): 
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
