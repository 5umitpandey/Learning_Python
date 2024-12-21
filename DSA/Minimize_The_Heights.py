#https://www.geeksforgeeks.org/problems/minimize-the-heights-i/1

def getMinDiff(self,arr,k):
        # code here
        n = len(arr)
        if( n == 1 ):
            return 0
        
        arr.sort()
        
        result = arr[n-1] - arr[0]
        
        smallest = arr[0] + k
        largest = arr[n-1] - k
        
        for i in range(0,n-1,1):
            minElement = min(smallest, arr[i+1] - k)
            maxElement = max(largest, arr[i] + k)
            
            result = min(result, maxElement - minElement)
        
        return result
