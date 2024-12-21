#https://www.geeksforgeeks.org/problems/maximum-product-subarray3604/1

def maxProduct(self,nums):
		# code here
        n = len(nums)
        if( n == 0 ):
            return 0
        
        maxProd = nums[0]
        minProd = nums[0]
        result = nums[0]
        
        for i in range(1,n,1):
            if( nums[i] < 0 ):
                maxProd, minProd = minProd, maxProd
            
            maxProd = max( nums[i], maxProd * nums[i] )
            minProd = min( nums[i], minProd * nums[i] )
            
            result = max(result, maxProd)
        
        return result
