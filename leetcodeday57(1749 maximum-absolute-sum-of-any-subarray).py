# You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

# Return the maximum absolute sum of any (possibly empty) subarray of nums.

# Note that abs(x) is defined as follows:

# If x is a negative integer, then abs(x) = -x.
# If x is a non-negative integer, then abs(x) = x.
 

# Example 1:

# Input: nums = [1,-3,2,3,-4]
# Output: 5
# Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.

# Example 2:
# Input: nums = [2,-5,1,-4,3,-2]
# Output: 8
# Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.
 

# Constraints:
# 1 <= nums.length <= 10^5
# -104 <= nums[i] <= 10^4

# Solution:---------------------------------------------------------------------

class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        maxs, mins = float('-inf'), float('inf')
        cur, curr = 0, 0
        for num in nums:
            cur += num
            curr += num
            maxs = max(cur, maxs)
            mins = min(curr, mins)
            if cur < 0:
                cur = 0
            if curr > 0:
                curr = 0
        return max(abs(mins), maxs)