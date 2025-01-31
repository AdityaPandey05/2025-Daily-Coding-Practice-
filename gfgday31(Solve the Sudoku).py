# Given an incomplete Sudoku configuration in terms of a 9x9  2-D interger square matrix, mat[][], the task is to solve the Sudoku. It is guaranteed that the input Sudoku will have exactly one solution.

# A sudoku solution must satisfy all of the following rules:

# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# Note: Zeros represent blanks to be filled with numbers 1-9, while non-zero cells are fixed and cannot be changed.

# Examples:

# Input: mat[][] = 

# Output:

# Explanation: Each row, column and 3 x 3 box of the output matrix contains unique numbers.
# Input: mat[][] = 

# Output:
# Explanation: Each row, column and 3 x 3 box of the output matrix contains unique numbers.


# Constraints:
# mat.size() = 9
# mat[i].size() = 9
# 0 ≤ mat[i][j] ≤ 9

# Solution:---------------------------------------------------------------------

class Solution:
    def solveSudoku(self, mat):
        # Helper sets to track numbers in rows, columns, and 3x3 boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []
        
        # Initialize sets with existing numbers
        for i in range(9):
            for j in range(9):
                if mat[i][j] == 0:
                    empty_cells.append((i, j))  # Store empty cell
                else:
                    val = mat[i][j]
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[(i//3) * 3 + (j//3)].add(val)

        # Recursive backtracking function
        def solve(index=0):
            if index == len(empty_cells):  # All cells filled
                return True
            
            r, c = empty_cells[index]
            box_idx = (r//3) * 3 + (c//3)

            for num in range(1, 10):
                if num not in rows[r] and num not in cols[c] and num not in boxes[box_idx]:
                    # Place number and update sets
                    mat[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_idx].add(num)

                    if solve(index + 1):  # Recursive call
                        return True

                    # Backtrack
                    mat[r][c] = 0
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box_idx].remove(num)

            return False  # No valid number found

        return solve()
    
    # Function to print the solved Sudoku grid
    def printGrid(self, grid):
        for row in grid:
            print(" ".join(map(str, row)))
