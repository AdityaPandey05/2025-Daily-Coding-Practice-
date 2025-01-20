# Given the head of two sorted linked lists consisting of nodes respectively. The task is to merge both lists and return the head of the sorted merged list.

# Examples:

# Input: head1 = 5 -> 10 -> 15 -> 40, head2 = 2 -> 3 -> 20
# Output: 2 -> 3 -> 5 -> 10 -> 15 -> 20 -> 40
# Explanation:

# Input: head1 = 1 -> 1, head2 = 2 -> 4
# Output: 1 -> 1 -> 2 -> 4
# Explanation:

# Constraints:
# 1 <= no. of nodes<= 10^3
# 0 <= node->data <= 10^5

# Solution:-------------------------------------------------------------------

class Solution:
    def sortedMerge(self,head1, head2):
        # code here
        c1 = head1
        c2 = head2
        res = Node(-1)
        r = res
        while c1 != None and c2 != None:
            
            if c1.data < c2.data:
                res.next = c1
                res = res.next
                c1 = c1.next
            else:
                res.next = c2
                res = res.next
                c2 = c2.next
        if c1 is None:
            res.next = c2
        if c2 is None:
            res.next = c1
        return r.next    
