# You have n  tiles, where each tile has one letter tiles[i] printed on it.

# Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

# Example 1:
# Input: tiles = "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

# Example 2:
# Input: tiles = "AAABBC"
# Output: 188

# Example 3:
# Input: tiles = "V"
# Output: 1

# Constraints:
# 1 <= tiles.length <= 7
# tiles consists of uppercase English letters.

# Solution:---------------------------------------------------------------------

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        return len(set(p for i in range(1, len(tiles)+1) for p in permutations(tiles, i)))