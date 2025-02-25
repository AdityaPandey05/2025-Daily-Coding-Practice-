# You are given a histogram represented by an array arr, where each element of the array denotes the height of the bars in the histogram. All bars have the same width of 1 unit.

# Your task is to find the largest rectangular area possible in the given histogram, where the rectangle can be formed using a number of contiguous bars.

# Examples:

# Input: arr[] = [60, 20, 50, 40, 10, 50, 60]
#  Largest-Rectangular-Area-in-a-Histogram
# Output: 100
# Explanation: We get the maximum by picking bars highlighted above in green (50, and 60). The area is computed (smallest height) * (no. of the picked bars) = 50 * 2 = 100.

# Input: arr[] = [3, 5, 1, 7, 5, 9]
# Output: 15
# Explanation:  We get the maximum by picking bars 7, 5 and 9. The area is computed (smallest height) * (no. of the picked bars) = 5 * 3 = 15.

# Input: arr[] = [3]
# Output: 3
# Explanation: In this example the largest area would be 3 of height 3 and width 1.

# Constraints:
# 1 ≤ arr.size() ≤ 10^5
# 0 ≤ arr[i] ≤ 10^4

# Solution:-----------------------------------------------------------------

class Solution:
    def getMaxArea(self,arr):
        n = len(arr)
        right = [n]*n
        
        stack = []
        for i, e in enumerate(arr):
            while stack and arr[stack[-1]] > e:
                right[stack.pop()] = i
            stack.append(i)
        
        #print(right)
        stack = []
        left = [-1]*n
        for i in range(len(arr)-1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                left[stack.pop()] = i
            stack.append(i)
        
        #print(left)
        ans = 0
        for i in range(n):
            w = right[i]-left[i] - 1
            ans = max(ans, arr[i]*w)
        return ans