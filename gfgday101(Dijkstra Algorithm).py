import heapq
from collections import defaultdict
class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # code here
        l=defaultdict(list)
        for i,j,k in edges:
            l[i].append((j,k))
            l[j].append((i,k))


        r=[float('inf')]*V
        r[src]=0
        s=[(0,src)]


        while s:
            t1,t2=heapq.heappop(s)
            if t1>r[t2]:continue
            for j,k in l[t2]:
                if r[t2]+k<r[j]:
                    r[j]=r[t2]+k
                    heapq.heappush(s,(r[j],j))


        return r
