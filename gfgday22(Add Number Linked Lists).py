# Given the head of two singly linked lists num1 and num2 representing two non-negative integers. The task is to return the head of the linked list representing the sum of these two numbers.

# For example, num1 represented by the linked list : 1 -> 9 -> 0, similarly num2 represented by the linked list: 2 -> 5. Sum of these two numbers is represented by 2 -> 1 -> 5.

# Note: There can be leading zeros in the input lists, but there should not be any leading zeros in the output list.

# Examples:

# Input: num1 = 4 - > 5, num2 = 3 -> 4 -> 5
# Output:  3 -> 9 -> 0
 
# Explanation: Given numbers are 45 and 345. There sum is 390.
# Input: num1 = 0 -> 0 -> 6 -> 3, num2 = 0 -> 7 
# Output: 7 -> 0 
 
# Explanation: Given numbers are 63 and 7. There sum is 70.
# Constraints:
# 1 <= size of both linked lists <= 10^6
# 0 <= elements of both linked lists <= 9

# Solution:---------------------------------------------------------------------


class Solution:
    def addTwoLists(self, num1, num2):
        def rev(head):
            prv=None
            cur=head
            while cur:
                tmp=cur.next
                cur.next=prv
                prv=cur
                cur=tmp
            return prv
        num1=rev(num1)
        num2=rev(num2)
        carry=0
        ret=Node(0)
        cur=ret
        while num1 or num2 or carry:
            ve=(num1.data if num1 else 0)+(num2.data if num2 else 0)+carry
            cur.data=ve%10
            carry=1 if ve>=10 else 0
            num1=num1.next if num1 else None
            num2=num2.next if num2 else None
            cur.next=Node(0)
            cur=cur.next
        ret=rev(ret)
        while ret.data==0:
            ret=ret.next
        return ret