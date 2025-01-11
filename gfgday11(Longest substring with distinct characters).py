# Given a string s, find the length of the longest substring with all distinct characters. 

# Examples:

# Input: s = "geeksforgeeks"
# Output: 7
# Explanation: "eksforg" is the longest substring with all distinct characters.


# Input: s = "aaa"
# Output: 1
# Explanation: "a" is the longest substring with all distinct characters.

# Input: s = "abcdefabcbb"
# Output: 6
# Explanation: The longest substring with all distinct characters is "abcdef", which has a length of 6.

# Constraints:
# 1<= s.size()<=3*104
# All the characters are in lowercase.

# Solution:--------------------------------------------------------

class Solution:
    def longestUniqueSubstr(self, s):
     
        mp = {}
        l, ans = 0, 0
        for r in range(len(s)):
            mp[s[r]] = mp.get(s[r], 0) + 1
            
            while mp[s[r]] > 1:
                mp[s[l]] = mp.get(s[l], 0) - 1
                l += 1
                
            ans = max(ans, r - l + 1)
        
        return ans