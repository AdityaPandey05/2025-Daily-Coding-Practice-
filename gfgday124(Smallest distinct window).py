from collections import defaultdict
class Solution:
    def findSubString(self, str):
        # code here
        ans = n = len(str) # whole string is maximum sized window containing all letters
        k = len(set(str)) # number of unique letters
        d = defaultdict(int) # dict with 'int' as defaultfactory
        i = 0
        for j,char in enumerate(str):
            if not d[char]: # first entry
                k -= 1
            d[char] += 1
            while not k: # d contains all unique letters of str
                ans = min(ans, j-i+1)
                d[str[i]] -= 1
                if not d[str[i]]:
                    k = 1 # equivalent to k += 1
                i += 1
        return ans
