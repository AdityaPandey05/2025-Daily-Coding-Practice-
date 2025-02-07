# gfg daily day 37 feb 6
# Given two arrays representing the inorder and preorder traversals of a binary tree, construct the tree and return the root node of the constructed tree.

# Note: The output is written in postorder traversal.

# Examples:

# Input: inorder[] = [1, 6, 8, 7], preorder[] = [1, 6, 7, 8]
# Output: [8, 7, 6, 1]


# Input: inorder[] = [3, 1, 4, 0, 2, 5], preorder[] = [0, 1, 3, 4, 2, 5]
# Output: [3, 4, 1, 5, 2, 0]


# Input: inorder[] = [2, 5, 4, 1, 3], preorder[] = [1, 4, 5, 2, 3]
# Output: [2, 5, 4, 3, 1]


# Constraints:
# 1 ≤ number of nodes ≤ 10^3
# 0 ≤ nodes -> data ≤ 10^3
# Both the inorder and preorder arrays contain unique values.

# Solution:----------------------------------------------------------------------------------------------------------------------------------------------------------------


class Solution:
    def buildTree(self, inorder, preorder):
        
        index_map = { inorder[i] : i for i in range(len(inorder)) }
        pre_inx = 0
        
        def construct(left , right):
            nonlocal pre_inx
            if left> right:
                return None
            
            val = preorder[pre_inx]
            pre_inx+=1
            inorder_inx = index_map[val]
            root = Node(val)
            root.left = construct(left , inorder_inx-1)
            root.right = construct(inorder_inx+1,right)
            
            return root            
            
        return construct(0,len(inorder)-1)
