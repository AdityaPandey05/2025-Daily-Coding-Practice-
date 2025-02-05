#gfg day 36 feb 5 

# Given a binary tree, convert the binary tree to its Mirror tree.

# Mirror of a Binary Tree T is another Binary Tree M(T) with left and right children of all non-leaf nodes interchanged.     

# Examples:

# Input: root[] = [1, 2, 3, N, N, 4]
# Output: [1, 3, 2, N, 4]
# Explanation: In the inverted tree, every non-leaf node has its left and right child interchanged.

# Constraints:
# 1 ≤ number of nodes ≤ 10^5
# 1 ≤ node->data ≤ 10^5

# Solution:--------------------------------------------------------------------------------------------------------------------------------

class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self, root):
        # Code here
        if not root or (not root.left and not root.right): return 
        root.left,root.right=root.right,root.left
        self.mirror(root.left)
        self.mirror(root.right)
