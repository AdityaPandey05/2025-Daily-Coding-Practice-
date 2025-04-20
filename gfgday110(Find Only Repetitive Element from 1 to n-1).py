class Solution:
   
   def findDuplicate(self, arr):
        n=max(arr)
        return abs(sum(arr)-(n*(n+1)//2))
