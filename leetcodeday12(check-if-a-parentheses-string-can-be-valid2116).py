# A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:

# It is ().
# It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
# It can be written as (A), where A is a valid parentheses string.
# You are given a parentheses string s and a string locked, both of length n. locked is a binary string consisting only of '0's and '1's. For each index i of locked,

# If locked[i] is '1', you cannot change s[i].
# But if locked[i] is '0', you can change s[i] to either '(' or ')'.
# Return true if you can make s a valid parentheses string. Otherwise, return false.

 

# Example 1:


# Input: s = "))()))", locked = "010100"
# Output: true
# Explanation: locked[1] == '1' and locked[3] == '1', so we cannot change s[1] or s[3].
# We change s[0] and s[4] to '(' while leaving s[2] and s[5] unchanged to make s valid.

# Example 2:

# Input: s = "()()", locked = "0000"
# Output: true
# Explanation: We do not need to make any changes because s is already valid.

# Example 3:

# Input: s = ")", locked = "0"
# Output: false
# Explanation: locked permits us to change s[0]. 
# Changing s[0] to either '(' or ')' will not make s valid.
 

# Constraints:

# n == s.length == locked.length
# 1 <= n <= 10^5
# s[i] is either '(' or ')'.
# locked[i] is either '0' or '1'.

# Solution:------------------------------------------------------

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False

        open_count = 0
        for i in range(n):
            if s[i] == '(' or locked[i] == '0':
                open_count += 1
            else:
                open_count -= 1
            if open_count < 0:
                return False

        close_count = 0
        for i in range(n - 1, -1, -1):
            if s[i] == ')' or locked[i] == '0':
                close_count += 1
            else:
                close_count -= 1
            if close_count < 0:
                return False

        return True

#Approach:
   
# Check from left to right:

# Traverse the string, treating every ( and unlocked position (0) as potential open brackets.
# If the number of close brackets ) exceeds the available open brackets, the string cannot be valid.
# Check from right to left:

# Traverse the string in reverse, treating every ) and unlocked position (0) as potential close brackets.
# If the number of open brackets ( exceeds the available close brackets, the string cannot be valid.
# If both passes succeed, it means the flexible positions can accommodate the required parentheses to balance the string.

# Complexity
# Time complexity:
# O(n) - Each pass (left-to-right and right-to-left) processes the string in linear time.

# Space complexity:
# O(1) - No additional space is used other than a few integer counters.