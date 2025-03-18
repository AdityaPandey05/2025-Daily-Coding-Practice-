class Solution:
   def longestNiceSubarray(self, nums: List[int]) -> int:
    l = 0
    bit_mask = 0
    max_length = 0

    for r in range(len(nums)):
        while (bit_mask & nums[r]) != 0:
            bit_mask ^= nums[l]  # Remove nums[l] from mask
            l += 1
        bit_mask |= nums[r]  # Add nums[r] to mask
        max_length = max(max_length, r - l + 1)

    return max_length
