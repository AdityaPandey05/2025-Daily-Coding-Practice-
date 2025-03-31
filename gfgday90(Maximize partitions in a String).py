class Solution:
    def maxPartitions(self , s):
        intervals = {c:i for i,c in enumerate(s)}
        # print(intervals)
        
        f_max=-1
        cnt=0
        
        for i,c in enumerate(s):
            
            f_max=max(f_max,intervals[c])
            
            if f_max==i:
                cnt+=1
                
        return cnt
