class Solution:  
    def findMaxSum(self,arr):
        # code here
        n = len(arr)
        if n == 0:
            return 0
        if n ==1:
            return arr[0]
        prev1 = arr[0]
        prev2 = max(arr[0], arr[1])
        
        for i in range(2, n):
            cur = max(prev2, arr[i]+ prev1)
            prev1 = prev2
            prev2= cur
            
        return prev2