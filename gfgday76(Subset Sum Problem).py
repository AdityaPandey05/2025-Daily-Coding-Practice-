from functools import reduce
class Solution:
    def isSubsetSum (self, arr, sum):
        # code here 
        return(reduce(lambda x, y: x|(x<<y), [1]+arr) & (1<<sum)) > 0   
