class Solution:
    def maxXor(self, arr):
        lth=len(bin(max(arr,key=lambda x:len(bin(x)))))-2
        from collections import defaultdict
        v2b=defaultdict(list)
        root={}
        for ve in arr:
            ori=ve
            cur=root
            for pl in range(lth,-1,-1):
                val=1<<pl
                if val&ve:
                    v2b[ori].append(1)
                    if 1 not in cur:
                        cur[1]={}
                    cur=cur[1]
                else:
                    v2b[ori].append(0)
                    if 0 not in cur:
                        cur[0]={}
                    cur=cur[0]
                ve-=val
        mx=0
        for ve in arr:
            sm=0
            cur=root
            val=1<<lth
            for i in range(lth+1):
                b=v2b[ve][i]
                bneg=1 if b==0 else 0
                if bneg in cur:
                    sm+=val
                    cur=cur[bneg]
                elif b in cur:
                    cur=cur[b]
                val>>=1
            mx=max(mx,sm)
        return mx
        #code here
