class Solution:
    def equalPartition(self, arr):
        total_sum = sum(arr)
        if total_sum % 2 != 0:
          return False  # If sum is odd, can't partition

        target = total_sum // 2
        dp = [False] * (target + 1)
        dp[0] = True  # Base case: sum 0 is always possible

        for num in arr:
          for j in range(target, num - 1, -1):  # Traverse backwards to avoid reuse
              dp[j] = dp[j] or dp[j - num]

        return dp[target]
