# Given a string s consisting of opening and closing parenthesis '(' and ')'. Find the length of the longest valid parenthesis substring.

# A parenthesis string is valid if:

# For every opening parenthesis, there is a closing parenthesis.
# The closing parenthesis must be after its opening parenthesis.
# Examples :

# Input: s = "((()"
# Output: 2
# Explanation: The longest valid parenthesis substring is "()".

# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parenthesis substring is "()()".

# Input: s = "())()"
# Output: 2
# Explanation: The longest valid parenthesis substring is "()".

# Constraints:
# 1 ≤ s.size() ≤ 10^6  
# s consists of '(' and ')' only

# Solution:---------------------------------------------------------------------

class Solution:
    def maxLength(self, s):
        max_len = 0
        stack = [-1]

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len