class Solution:
    def countSubarrays(self, nums):
        index = 0
        for i in range(1, len(nums) - 1):
            if nums[i - 1] + nums[i + 1] == nums[i] / 2.0:
                index += 1
        return index
