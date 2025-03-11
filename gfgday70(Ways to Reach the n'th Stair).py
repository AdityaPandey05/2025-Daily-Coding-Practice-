# There are n stairs, a person standing at the bottom wants to reach the top. The person can climb either 1 stair or 2 stairs at a time.
# Your task is to count the number of ways, the person can reach the top (order does matter).

# Examples:
# Input: n = 1
# Output: 1
# Explanation: There is only one way to climb 1 stair. 

# Input: n = 2
# Output: 2
# Explanation: There are 2 ways to reach 2th stair: {1, 1} and {2}.

# Input: n = 4
# Output: 5
# Explanation: There are five ways to reach 4th stair: {1, 1, 1, 1}, {1, 1, 2}, {2, 1, 1}, {1, 2, 1} and {2, 2}.

# Constraints:
# 1 ≤ n ≤ 44

# Solution:------------------------------------------------------------------------------------------------------------------------

class Solution:
    def countWays(self, n):
        def f(n):
            if n < 0:
                return 0
            if n == 0:
                return 1
            if n in dp:
                return dp[n]
            dp[n] = f(n-1) + f(n-2)
            return dp[n]
        dp = {}
        return f(n)
