from collections import deque

class Solution:
    def isHeap(self, root):
        if not root:
            return True

        # Level order traversal to check CBT
        q = deque()
        q.append(root)
        end = False

        while q:
            node = q.popleft()
            if node.left:
                if end:
                    return False
                if node.data < node.left.data:
                    return False
                q.append(node.left)
            else:
                end = True

            if node.right:
                if end:
                    return False
                if node.data < node.right.data:
                    return False
                q.append(node.right)
            else:
                end = True

        return True
