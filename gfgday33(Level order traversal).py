# Given a root of a binary tree with n nodes, the task is to find its level order traversal. Level order traversal of a tree is breadth-first traversal for the tree.

# Examples:
# Input: root[] = [1, 2, 3]
# Output: [[1], [2, 3]]

# Input: root[] = [10, 20, 30, 40, 50]
# Output: [[10], [20, 30], [40, 50]]

# Input: root[] = [1, 3, 2, N, N, N, 4, 6, 5]
# Output: [[1], [3, 2], [4], [6, 5]]

# Constraints:
# 1 ≤ number of nodes ≤ 10^5
# 0 ≤ node->data ≤ 10^9

# Solution:---------------------------------------------------------------------

import collections

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        
        res = []
        q = collections.deque([root])

        while q:
            qLen = len(q)
            level = []
            for _ in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.data)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if level:  # Avoid adding empty levels
                res.append(level)
        
        return res