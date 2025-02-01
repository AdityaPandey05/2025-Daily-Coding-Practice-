# You are given a two-dimensional mat[][] of size n*m containing English alphabets and a string word. Check if the word exists on the mat. The word can be constructed by using letters from adjacent cells, either horizontally or vertically. The same cell cannot be used more than once.


# Examples :
# Input: mat[][] = [['T', 'E', 'E'], ['S', 'G', 'K'], ['T', 'E', 'L']], word = "GEEK"
# Output: true
# Explanation:
# The letter cells which are used to construct the "GEEK" are colored.

# Input: mat[][] = [['T', 'E', 'U'], ['S', 'G', 'K'], ['T', 'E', 'L']], word = "GEEK"
# Output: false
# Explanation:
# It is impossible to construct the string word from the mat using each cell only once.

# Input: mat[][] = [['A', 'B', 'A'], ['B', 'A', 'B']], word = "AB"
# Output: true
# Explanation:
# There are multiple ways to construct the word "AB".

# Constraints:
# 1 ≤ n, m ≤ 100
# 1 ≤ L ≤ n*m

# Solution:---------------------------------------------------------------------

class Solution:
    def isWordExist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def isWordFound(row, col, index, visited):
            if index == len(word):
                return True
            if (row < 0 or col < 0 or row >= rows or col >= cols or 
                (row, col) in visited or board[row][col] != word[index]):
                return False
            
            visited.add((row, col))
            found = (isWordFound(row, col + 1, index + 1, visited) or
                     isWordFound(row, col - 1, index + 1, visited) or
                     isWordFound(row + 1, col, index + 1, visited) or
                     isWordFound(row - 1, col, index + 1, visited))
            visited.remove((row, col))
            
            return found
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0] and isWordFound(row, col, 0, set()):
                    return True
        
        return False