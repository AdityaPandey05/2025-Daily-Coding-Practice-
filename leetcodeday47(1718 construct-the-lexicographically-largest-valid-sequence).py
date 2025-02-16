# Given an integer n, find a sequence that satisfies all of the following:

# The integer 1 occurs once in the sequence.
# Each integer between 2 and n occurs twice in the sequence.
# For every integer i between 2 and n, the distance between the two occurrences of i is exactly i.
# The distance between two numbers on the sequence, a[i] and a[j], is the absolute difference of their indices, |j - i|.

# Return the lexicographically largest sequence. It is guaranteed that under the given constraints, there is always a solution.

# A sequence a is lexicographically larger than a sequence b (of the same length) if in the first position where a and b differ, sequence a has a number greater than the corresponding number in b. For example, [0,1,9,0] is lexicographically larger than [0,1,5,6] because the first position they differ is at the third number, and 9 is greater than 5. 

# Example 1:
# Input: n = 3
# Output: [3,1,2,3,2]
# Explanation: [2,3,2,1,3] is also a valid sequence, but [3,1,2,3,2] is the lexicographically largest valid sequence.


# Example 2:
# Input: n = 5
# Output: [5,3,1,4,3,5,2,4,2]
 
# Constraints:
# 1 <= n <= 20

# Solution:---------------------------------------------------------------------

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        result = [0] * (2 * n - 1)
        used = [False] * (n + 1)
        self.backtrack(result, used, n, 0)
        return result

    def backtrack(self, result: List[int], used: List[bool], n: int, index: int) -> bool:
        while index < len(result) and result[index] != 0:
            index += 1
        if index == len(result):
            return True

        for i in range(n, 0, -1):
            if used[i]:
                continue

            if i == 1:
                result[index] = 1
                used[1] = True
                if self.backtrack(result, used, n, index + 1):
                    return True
                result[index] = 0
                used[1] = False
            elif index + i < len(result) and result[index + i] == 0:
                result[index] = i
                result[index + i] = i
                used[i] = True
                if self.backtrack(result, used, n, index + 1):
                    return True
                result[index] = 0
                result[index + i] = 0
                used[i] = False

        return False