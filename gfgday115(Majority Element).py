class Solution:
    def majorityElement(self, arr):
        d={}
        n=len(arr)
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
       
        for i in d:
            if d[i]>(n//2):
                return i
        return -1
