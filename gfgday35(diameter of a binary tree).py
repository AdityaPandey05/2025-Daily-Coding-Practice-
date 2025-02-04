(* # GFG DAILY 4th Feb Day 35
# Diameter of a binary tree  *)

(* Given a binary tree, the diameter (also known as the width) is defined as the number of edges on the longest path between two leaf nodes in the tree. This path may or may not pass through the root. Your task is to find the diameter of the tree.

Examples:

Input: root[] = [1, 2, 3]

Output: 2
Explanation: The longest path has 2 edges (node 2 -> node 1 -> node 3).

Input: root[] = [5, 8, 6, 3, 7, 9]

Output: 4
Explanation: The longest path has 4 edges (node 3 -> node 8 -> node 5 -> node 6 -> node 9).

Constraints:
1 ≤ number of nodes ≤ 10^5
0 ≤ node->data ≤ 10^5 *)

Solution:-----------------------------------------------------------------------------------------------------------------------------------------

class Solution:
    def solve(self,root,ans):
     if root:
        l=self.solve(root.left,ans)
        r=self.solve(root.right,ans)
        ans[0]=max(ans[0],l+r)
        return 1+max(l,r)
     return 0

    def diameter(self, root):
      ans=[0]
      self.solve(root,ans)
      return ans[0]

