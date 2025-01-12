# Given an array arr[] with non-negative integers representing the height of blocks. If the width of each block is 1, compute how much water can be trapped between the blocks during the rainy season. 

# Examples:

# Input: arr[] = [3, 0, 1, 0, 4, 0 2]
# Output: 10
# Explanation: Total water trapped = 0 + 3 + 2 + 3 + 0 + 2 + 0 = 10 units.

# Input: arr[] = [3, 0, 2, 0, 4]
# Output: 7
# Explanation: Total water trapped = 0 + 3 + 1 + 3 + 0 = 7 units.

# Input: arr[] = [1, 2, 3, 4]
# Output: 0
# Explanation: We cannot trap water as there is no height bound on both sides.

# Input: arr[] = [2, 1, 5, 3, 1, 0, 4]
# Output: 9
# Explanation: Total water trapped = 0 + 1 + 0 + 1 + 3 + 4 + 0 = 9 units.

# Constraints:
# 1 < arr.size() < 10^5
# 0 < arr[i] < 10^3

# Solution:------------------------------------------------------------- 

class Solution:
    def maxWater(self, arr):
        n=len(arr)
        waterFill=0
        lmax,rmax=0,0
        st,end=0,n-1
        while st<end:
            if arr[st]<arr[end]:
                if arr[st]<lmax:
                    waterFill+=lmax-arr[st]
                else:
                    lmax=arr[st]
                st+=1
            else:
                if arr[end]<rmax:
                    waterFill+=rmax-arr[end]
                else:
                    rmax=arr[end]
                end-=1
        return waterFill
      
# Approach dry run:------------ Two - pointer approach 


# Input: arr = [3, 0, 1, 0, 4, 0, 2]
# Output: 10

# Initial Setup:

# lmax = 0, rmax = 0, st = 0, end = 6, waterFill = 0.
# First Iteration:

# arr[st] = 3, arr[end] = 2 → arr[st] >= arr[end].
# Update rmax = max(0, 2) = 2.
# Move end to 5.
# Second Iteration:

# arr[st] = 3, arr[end] = 0 → arr[st] >= arr[end].
# Water trapped: rmax - arr[end] = 2 - 0 = 2.
# Add 2 to waterFill: waterFill = 2.
# Move end to 4.
# Third Iteration:

# arr[st] = 3, arr[end] = 4 → arr[st] < arr[end].
# Update lmax = max(0, 3) = 3.
# Move st to 1.
# Continue Similarly:

# The algorithm continues comparing, updating lmax and rmax, and calculating water trapped.
# Final result: waterFill = 10.


      