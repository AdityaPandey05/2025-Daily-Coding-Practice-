# Given an array of positive integers arr[] and a non-negative integer x, the task is to find the longest sub-array where the absolute difference between any two elements is not greater 
# than x. If multiple such subarrays exist, return the one that starts at the smallest index.

# Examples: 

# Input: arr[] = [8, 4, 2, 6, 7], x = 4 
# Output: [4, 2, 6] 
# Explanation: The sub-array described by index [1..3], i.e. [4, 2, 6] contains no such difference of two elements which is greater than 4.
  
# Input: arr[] = [15, 10, 1, 2, 4, 7, 2], x = 5 
# Output: [2, 4, 7, 2] 
# Explanation: The sub-array described by indexes [3..6], i.e. [2, 4, 7, 2] contains no such difference of two elements which is greater than 5. 
  
# Constraints:
# 1 <= arr.size() <= 10^5
# 1 <= arr[i] <= 10^9
# 0 <= x<= 10^9

# Solution:----------------------------------------------------------------------------------------------------------------------------------------------

class Solution:
    def longestSubarray(self, arr, x):
        from heapq import heappop, heappush
        min_h, max_h = [], []
        max_start = max_end = start = 0
        for end, a in enumerate(arr):
            heappush(min_h, (a, end))
            heappush(max_h, (-a, end))
            while -max_h[0][0] - min_h[0][0] > x:
                h = min_h if min_h[0][1] <= max_h[0][1] else max_h
                if h[0][1] >= start:
                    start = h[0][1] + 1
                heappop(h)
            if end - start > max_end - max_start:
                max_start, max_end = start, end
        return arr[max_start:max_end + 1]
