import heapq
class Solution:
    def printKClosest(self, arr, k, x):
        # code here
        l=[]
        for i in arr:
            if i!=x:
                heapq.heappush(l,(abs(i-x),-i))
        r=[]
        while l and k>0:
            _,i=heapq.heappop(l)
            r.append(-i)
            k-=1
        return r
