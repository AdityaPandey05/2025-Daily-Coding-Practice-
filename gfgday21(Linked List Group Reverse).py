# Given the head a linked list, the task is to reverse every k node in the linked list. If the number of nodes is not a multiple of k then the left-out nodes in the end, should be considered as a group and must be reversed.

# Examples:

# Input: head = 1 -> 2 -> 2 -> 4 -> 5 -> 6 -> 7 -> 8, k = 4
# Output: 4 -> 2 -> 2 -> 1 -> 8 -> 7 -> 6 -> 5

# Explanation: The first 4 elements 1, 2, 2, 4 are reversed first and then the next 4 elements 5, 6, 7, 8. Hence, the resultant linked list is 4 -> 2 -> 2 -> 1 -> 8 -> 7 -> 6 -> 5.


# Input: head = 1 -> 2 -> 3 -> 4 -> 5, k = 3
# Output: 3 -> 2 -> 1 -> 5 -> 4

# Explanation: The first 3 elements 1, 2, 3 are reversed first and then left out elements 4, 5 are reversed. Hence, the resultant linked list is 3 -> 2 -> 1 -> 5 -> 4.


# Constraints:
# 1 <= size of linked list <= 10^5
# 1 <= data of nodes <= 10^6
# 1 <= k <= size of linked list 

# Solution:----------------------------------------------------------------

class Solution:
    def reverseKGroup(self, head, k):
        
        def findKthNode(node):
            count=1
            curr=node
            while curr and curr.next and count<k:
                curr=curr.next
                count+=1
            
            return curr
            
        def reverse(node):
            curr=node
            prev=None
            while curr:
                nextt=curr.next
                curr.next=prev
                prev=curr
                curr=nextt
                
            return prev
        
        temp=head
        while (temp):
            kthNode=findKthNode(temp)
            nextNode=kthNode.next
            kthNode.next=None
            
            reverse(temp)
            if (temp==head):
                head=kthNode
            else:
                prevNode.next=kthNode
            
            prevNode=temp
            temp=nextNode
        
        return head