# Given the head of a singly linked list, your task is to left rotate the linked list k times.

# Examples:

# Input: head = 10 -> 20 -> 30 -> 40 -> 50, k = 4
# Output: 50 -> 10 -> 20 -> 30 -> 40
# Explanation:
# Rotate 1: 20 -> 30 -> 40 -> 50 -> 10
# Rotate 2: 30 -> 40 -> 50 -> 10 -> 20
# Rotate 3: 40 -> 50 -> 10 -> 20 -> 30
# Rotate 4: 50 -> 10 -> 20 -> 30 -> 40

# Input: head = 10 -> 20 -> 30 -> 40 , k = 6
# Output: 30 -> 40 -> 10 -> 20 
 
# Constraints:

# 1 <= number of nodes <= 10^5
# 0 <= k <= 10^9
# 0 <= data of node <= 10^9 

# Solution:---------------------------------------------------------------------

class Solution:
    
    #Function to rotate a linked list.
  def rotate(self, head, k):
    if not head or not head.next or k == 0:
     return head
    
    # Step 1: Find the length of the linked list
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1
    
    # Step 2: Compute effective rotations
    k = k % length
    if k == 0:
        return head  # No rotation needed
    
    # Step 3: Traverse to the k-th node
    prev = None
    current = head
    for _ in range(k):
        prev = current
        current = current.next
    
    # Step 4: Rearrange the list
    prev.next = None  # Break the list
    tail.next = head  # Link the tail to the original head
    
    # Step 5: Return the new head
    return current