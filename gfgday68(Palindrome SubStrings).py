# Given a string s, count all palindromic sub-strings present in the string. The length of the palindromic sub-string must be greater than or equal to 2. 

# Examples

# Input: s = "abaab"
# Output: 3
# Explanation: All palindromic substrings are : "aba" , "aa" , "baab".

# Input: s = "aaa"
# Output: 3
# Explanation: All palindromic substrings are : "aa", "aa", "aaa".

# Input: s = "abbaeae"
# Output: 4
# Explanation: All palindromic substrings are : "bb" , "abba" , "aea", "eae".

# Constraints:
# 2 ≤ s.size() ≤ 10^3
# string contains only lowercase english characters

# Solution:--------------------------------------------------------------------------------------------------------------------------------------

class Solution:

  def countPS(self, s):
    n=len(s)
    ans=0
    for i in range(n):
        for h in (i,i+1):
            l=i-1
            while l>=0 and h<n and s[l]==s[h]:
                l-=1
                h+=1
                ans+=1
    return ans
