class Solution:
 def minJumps(self, arr):
	n=len(arr)
    jumps,maxRange,currRange=0,0,0
    for i in range(n-1):
        maxRange=max(maxRange,arr[i]+i)
        if i==currRange:
            if maxRange<=i:
                return -1
            currRange=maxRange
            jumps+=1
    return jumps
