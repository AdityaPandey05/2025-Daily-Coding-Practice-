# Implement the function power(b, e), which calculates b raised to the power of e (i.e. be).

# Examples:

# Input: b = 3.00000, e = 5
# Output: 243.00000


# Input: b = 0.55000, e = 3
# Output: 0.16638


# Input: b = -0.67000, e = -7
# Output: -16.49971


# Constraints:

# -100.0 < b < 100.0
# -10^9 <= e <= 10^9
# Either b is not zero or e > 0.
# -10^4 <= be <= 10^4

# Solution:---------------------------------------------------------------------

class Solution:
    def power(self, b: float, e: int) -> float:
        if e == 0:
         return 1.0  # Any number raised to the power 0 is 1
    
        negative_exponent = e < 0
        e = abs(e)
    
        result = 1.0
        while e:
          if e % 2 == 1:  # If exponent is odd, multiply the base
            result *= b
          b *= b  # Square the base
          e //= 2  # Reduce exponent by half
    
        return result if not negative_exponent else 1 / result  # Handle negative exponents