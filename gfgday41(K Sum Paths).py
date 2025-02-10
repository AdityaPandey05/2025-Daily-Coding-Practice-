# Given a binary tree and an integer k, determine the number of downward-only paths where the sum of the node values in the path equals k. 
# A path can start and end at any node within the tree but must always move downward (from parent to child).

# Examples:

# Input: k = 7   
# Output: 3
# Explanation: The following paths sum to k 


# Input: k = 3
#    1
#   /  \
# 2     3
# Output: 2
# Explanation:
# Path 1 : 1 -> 2 (Sum = 3)
# Path 2 : 3 (Sum = 3)


# Constraints:
# 1 ≤ number of nodes ≤ 10^4
# -100 ≤ node value ≤ 100
# -10^9 ≤ k ≤ 10^9

# SOLUTION:-----------------------------------------------------------------------------------------------------------------------------------------------------------------

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def sumK(self, root, k):
        # code here
        def explorePaths(node, currentTotal, prefixSums):
            if node is None:
                return 0

            currentTotal += node.data
            pathCount = prefixSums.get(currentTotal - k, 0)

            # Update prefix sums dictionary
            prefixSums[currentTotal] = prefixSums.get(currentTotal, 0) + 1

            # Recur for left and right subtrees
            leftPaths = explorePaths(node.left, currentTotal, prefixSums)
            rightPaths = explorePaths(node.right, currentTotal, prefixSums)

            # Backtrack by removing the current sum entry
            prefixSums[currentTotal] -= 1
            if prefixSums[currentTotal] == 0:
                del prefixSums[currentTotal]

            return pathCount + leftPaths + rightPaths

        prefixSums = {0: 1}
        return explorePaths(root, 0, prefixSums)
