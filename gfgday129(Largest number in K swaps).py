class Solution:
    
    # Function to find the largest number after k swaps.
    def findMaximumNum(self, s, k):
        s = list(s)  # Convert string to list to allow swapping
        n = len(s)
        
        i = 0
        while i < n and k > 0:
            # Find the max digit from s[i] to s[n-1]
            max_digit = s[i]
            max_idx = i
            for j in range(n-1, i, -1):
                if s[j] > max_digit:
                    max_digit = s[j]
                    max_idx = j
            
            # If we found a larger digit to swap
            if max_idx != i:
                s[i], s[max_idx] = s[max_idx], s[i]
                k -= 1  # Used one swap
            i += 1  # Move to next digit

        return "".join(s)
