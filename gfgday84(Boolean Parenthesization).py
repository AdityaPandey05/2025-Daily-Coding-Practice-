# You are given a boolean expression s containing
#     'T' ---> true
#     'F' ---> false 
# and following operators between symbols
#    &   ---> boolean AND
#     |   ---> boolean OR
#    ^   ---> boolean XOR
# Count the number of ways we can parenthesize the expression so that the value of expression evaluates to true.

# Note: The answer is guaranteed to fit within a 32-bit integer.

# Examples:

# Input: s = "T|T&F^T"
# Output: 4
# Explaination: The expression evaluates to true in 4 ways: ((T|T)&(F^T)), (T|(T&(F^T))), (((T|T)&F)^T) and (T|((T&F)^T)).

# Input: s = "T^F|F"
# Output: 2
# Explaination: The expression evaluates to true in 2 ways: ((T^F)|F) and (T^(F|F)).

# Constraints:
# 1 ≤ |s| ≤ 100

# Solution: ---------------------------------------------------------------------------------------------------------------------------

class Solution:
    def countWays(self, s: str) -> int:
        memo = {}

        def ways(i, j, isTrue):
            if (i, j, isTrue) in memo:
                return memo[(i, j, isTrue)]

            # Base Case: Single character
            if i == j:
                if isTrue:
                    return 1 if s[i] == 'T' else 0
                else:
                    return 1 if s[i] == 'F' else 0

            totalWays = 0

            # Consider each operator at odd indices
            for k in range(i + 1, j, 2):
                leftTrue = ways(i, k - 1, True)
                leftFalse = ways(i, k - 1, False)
                rightTrue = ways(k + 1, j, True)
                rightFalse = ways(k + 1, j, False)

                if s[k] == '&':
                    if isTrue:
                        totalWays += leftTrue * rightTrue
                    else:
                        totalWays += leftFalse * rightFalse + leftTrue * rightFalse + leftFalse * rightTrue
                elif s[k] == '|':
                    if isTrue:
                        totalWays += leftTrue * rightTrue + leftTrue * rightFalse + leftFalse * rightTrue
                    else:
                        totalWays += leftFalse * rightFalse
                elif s[k] == '^':
                    if isTrue:
                        totalWays += leftTrue * rightFalse + leftFalse * rightTrue
                    else:
                        totalWays += leftTrue * rightTrue + leftFalse * rightFalse

            memo[(i, j, isTrue)] = totalWays
            return totalWays

        return ways(0, len(s) - 1, True)
