class Solution:
    def findMinCycle(self, V, edges):
        from collections import defaultdict
        from heapq import heappush, heappop
        
        g = defaultdict(list)
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))
        
        INF = float('inf')
        def dijkstra(g, src, target, banned_edge):
            nonlocal INF
            costs = [INF]*V 
            costs[src] = 0
            q = [(0, src)]
            
            while q:
                w0, u0 = heappop(q)
                if u0 == target:
                    return w0
                for v0, w in g.get(u0, []):
                    if sorted([u0, v0]) == sorted(banned_edge):
                        continue
                    if w0 + w < costs[v0]:
                        costs[v0] = w0 + w
                        heappush(q, (w0+w, v0))
            return INF
        
        ans = INF
        for u, v, w in edges:
            ans = min(ans, dijkstra(g, u, v, (u, v))+w)
        return ans
