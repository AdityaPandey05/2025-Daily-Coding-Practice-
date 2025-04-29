class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count=0
        mx=max(nums)
        left=0
        mxcnt=0
        for right in range(len(nums)):
            if nums[right]==mx:
                mxcnt+=1
            while mxcnt==k:
                count+=(len(nums)-right)
                if nums[left]==mx:
                    mxcnt-=1
                left+=1
        return count
        
