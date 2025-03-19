class Solution:
  def maxProfit(self, prices, k):
    if not prices:
        return 0
    
    n = len(prices)
    
    # If k is very large, it reduces to unlimited transactions problem
    if k >= n // 2:
        return sum(max(prices[i+1] - prices[i], 0) for i in range(n - 1))
    
    # DP Table
    dp = [[0] * n for _ in range(k + 1)]
    
    for i in range(1, k + 1):
        maxDiff = -prices[0]  # Initialize maxDiff for current transaction
        for j in range(1, n):
            dp[i][j] = max(dp[i][j-1], prices[j] + maxDiff)
            maxDiff = max(maxDiff, dp[i-1][j] - prices[j])
    
    return dp[k][n-1]
