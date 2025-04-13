class Solution():
    def cloneGraph(self, node):
        seen = {}
        def clone(n):
            if n in seen:
                return seen[n]
            cp = Node(n.val, [])
            seen[n] = cp
            for nbr in n.neighbors:
                cp.neighbors.append(clone(nbr))
            return cp
        return clone(node)
