# Given the head of a linked list, the task is to reverse this list and return the reversed head.

# Examples:

# Input: head: 1 -> 2 -> 3 -> 4 -> NULL
# Output: head: 4 -> 3 -> 2 -> 1 -> NULL
# Explanation:

# Input: head: 2 -> 7 -> 10 -> 9 -> 8 -> NULL
# Output: head: 8 -> 9 -> 10 -> 7 -> 2 -> NULL
# Explanation:

# Input: head: 2 -> NULL
# Output: 2 -> NULL
# Explanation:

# Constraints:
# 1 <= number of nodes, data of nodes <= 10^5

# Solution:-------------------------------------------------------------
class Solution:
  def reverseList(self, head):
    prev = None
    current = head
    
    while current:
        next_node = current.next  # Save the next node
        current.next = prev       # Reverse the link
        prev = current            # Move prev to current
        current = next_node       # Move current to next_node
    
    return prev  # pre