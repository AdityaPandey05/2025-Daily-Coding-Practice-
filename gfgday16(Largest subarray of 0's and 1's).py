# Given an array arr of 0s and 1s. Find and return the length of the longest subarray with equal number of 0s and 1s.

# Examples:

# Input: arr[] = [1, 0, 1, 1, 1, 0, 0]
# Output: 6
# Explanation: arr[1...6] is the longest subarray with three 0s and three 1s.

# Input: arr[] = [0, 0, 1, 1, 0]
# Output: 4
# Explnation: arr[0...3] or arr[1...4] is the longest subarray with two 0s and two 1s.

# Input: arr[] = [0]
# Output: 0
# Explnation: There is no subarray with an equal number of 0s and 1s.

# Constraints:
# 1 <= arr.size() <= 10^5
# 0 <= arr[i] <= 1

# Solution:--------------------------------------------------------------------

class Solution:
   def maxLen(self, arr):
    # Replace 0s with -1s
    n = len(arr)
    for i in range(n):
        if arr[i] == 0:
            arr[i] = -1
    
    prefix_sum = 0
    max_length = 0
    hashmap = {0: -1}  # To handle cases where the subarray starts from index 0

    for i in range(n):
        prefix_sum += arr[i]

        if prefix_sum in hashmap:
            # Calculate the length of the subarray
            length = i - hashmap[prefix_sum]
            max_length = max(max_length, length)
        else:
            # Store the first occurrence of this prefix_sum
            hashmap[prefix_sum] = i
    
    return max_length
        
#This approach runs in O(n)in time as well as O(n) in space for the hashmap approach.
