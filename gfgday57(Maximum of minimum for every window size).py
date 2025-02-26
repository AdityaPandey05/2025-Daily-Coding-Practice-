# Given an array of integers arr[], the task is to find the maximum of the minimum values for every possible window size in the array, where the window size ranges from 1 to arr.size().

# More formally, for each window size k, determine the smallest element in all windows of size k, and then find the largest value among these minimums where 1<=k<=arr.size().

# Examples :

# Input: arr[] = [10, 20, 30, 50, 10, 70, 30]
# Output: [70, 30, 20, 10, 10, 10, 10] 
# Explanation: 
# 1. First element in output indicates maximum of minimums of all windows of size 1. Minimums of windows of size 1 are [10], [20], [30], [50], [10], [70] and [30]. Maximum of these minimums is 70. 
# 2. Second element in output indicates maximum of minimums of all windows of size 2. Minimums of windows of size 2 are [10], [20], [30], [10], [10], and [30]. Maximum of these minimums is 30. 
# 3. Third element in output indicates maximum of minimums of all windows of size 3. Minimums of windows of size 3 are [10], [20], [10], [10] and [10]. Maximum of these minimums is 20. 
# Similarly other elements of output are computed.

# Input: arr[] = [10, 20, 30]
# Output: [30, 20, 10]
# Explanation: First element in output indicates maximum of minimums of all windows of size 1. Minimums of windows of size 1 are [10] , [20] , [30]. Maximum of these minimums are 30 and similarly other outputs can be computed

# Constraints:
# 1 <= arr.size() <= 10^5
# 1 <= arr[i] <= 10^6

# Solution:---------------------------------------------------------------------

class Solution:
    def maxOfMins(self, arr):
        # find the next/pre smaller elements
        # if the length = n window has min value x, 
        # then the length = n-1 window has min value >= x (at least x)
        n = len(arr)
        right = [n]*n
        stack = []
        for i, e in enumerate(arr):
            # don't use arr[stack[-1]] >= e since we are 
            # trying to find the longest window, the shorter 
            # window will automatically work and in the last 
            # step, we can use longest window min value for 
            # shorter window
            while stack and arr[stack[-1]] > e:
                right[stack.pop()] = i 
            stack.append(i)

        left = [-1]*n
        stack = []
        for i in range(n-1, -1, -1):
            e = arr[i]
            while stack and arr[stack[-1]] > e:
                left[stack.pop()] = i
            stack.append(i)

        ans = [0]*n
        for i in range(n-1, -1, -1):
            r = right[i]-left[i]-1
            ans[r-1] = max(ans[r-1], arr[i])

        #this line is not necessary since the minimum value
        #will always have length n
        #ans[-1] = min(arr)
        #print(ans)
        for i in range(n-2, -1, -1):
            ans[i] = max(ans[i], ans[i+1])
   
        return ans