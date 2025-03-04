# Given an array arr[] of non-negative integers, the task is to find the length of the Longest Strictly Increasing Subsequence (LIS).

# A subsequence is strictly increasing if each element in the subsequence is strictly less than the next element.

# Examples:

# Input: arr[] = [5, 8, 3, 7, 9, 1]
# Output: 3
# Explanation: The longest strictly increasing subsequence could be [5, 7, 9], which has a length of 3.

# Input: arr[] = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
# Output: 6
# Explanation: One of the possible longest strictly increasing subsequences is [0, 2, 6, 9, 13, 15], which has a length of 6.

# Input: arr[] = [3, 10, 2, 1, 20]
# Output: 3
# Explanation: The longest strictly increasing subsequence could be [3, 10, 20], which has a length of 3.

# Constraints:
# 1 ≤ arr.size() ≤ 10^3
# 0 ≤ arr[i] ≤ 10^6

# Solution:----------------------------------------------------------------------------------------------------------------------------------------

class Solution:
    def lis(self, arr):
        if not arr:
           return 0

        n = len(arr)
        dp = [1] * n  # Initialize all values as 1

        for i in range(n):
          for j in range(i):
            if arr[j] < arr[i]:  # Strictly increasing condition
                dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)  # The length of the longest increasing subsequence
