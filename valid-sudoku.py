"""
Determine if a Sudoku is valid, according to:
http://sudoku.com.au/TheRules.aspx.
The Sudoku board could be partially filled, where empty cells are filled
with the character '.'.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only
the filled cells need to be validated.
Problem found here:
https://oj.leetcode.com/problems/valid-sudoku/
"""




class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        if len(board) != 9:
            return False
        for row in board:
            if len(row) != 9:
                return False
        columns = [[] for i in xrange(9)]
        rows = [[] for i in xrange(9)]
        squares = [[] for i in xrange(9)]
        for y in xrange(9):
            for x in xrange(9):
                val = board[y][x]
                if val != '.':
                    if (val in columns[y] or val in rows[x]
                        or val in squares[(y)/3 + ((x)/3)*3]):
                            return False
                    columns[y].append(val)
                    rows[x].append(val)
                    squares[(y)/3 + ((x)/3)*3].append(val)
        return True


#test
sol = Solution()
print_sudoku = False
sudoku_list = [(
      [[2,9,'.','.','.','.','.',7,'.'],
       [3,'.',6,'.','.',8,4,'.','.'],
       [8,'.','.','.',4,'.','.','.',2],
       ['.',2,'.','.',3,1,'.','.',7],
       ['.','.','.','.',8,'.','.','.','.'],
       [1,'.','.',9,5,'.','.',6,'.'],
       [7,'.','.','.',9,'.','.','.',1],
       ['.','.',1,2,'.','.',3,'.',6],
       ['.',3,'.','.','.','.','.',5,9]], True),
    ([['.', 9, 4, '.', '.', '.', 1, 3, '.'],
      ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
      ['.', '.', '.', '.', 7, 6, '.', '.', 2],
      ['.', 8, '.', '.', 1, '.', '.', '.', '.'],
      ['.', 3, 2, '.', '.', '.', '.', '.', '.'],
      ['.', '.', '.', 2, '.', '.', '.', 6, '.'],
      ['.', '.', '.', '.', 5, '.', 4, '.', '.'],
      ['.', '.', '.', '.', '.', 8, '.', '.', 7],
      ['.', '.', 6, 3, '.', 4, '.', '.', 8]], True),
    ([['.', '.', '.', '.', '.', '.', '.', '.', '.'],
      ['.', '.', '.', 9, 4, 2, '.', 8, '.'],
      [1, 6, '.', '.', '.', '.', '.', 2, 9],
      ['.', '.', '.', '.', '.', '.', '.', '.', 8],
      [9, '.', 6, '.', '.', '.', '.', '.', 1],
      [4, '.', '.', 2, 5, '.', '.', '.', '.'],
      ['.', '.', 4, '.', '.', '.', '.', '.', '.'],
      ['.', 2, '.', '.', '.', 8, '.', 9, '.'],
      ['.', 5, '.', '.', '.', '.', 7, '.', '.']], True),
    ([['.', '.', '.', '.', '.', 7, '.', '.', '.'],
      ['.', 9, '.', '.', '.', 1, '.', '.', '.'],
      ['.', '.', '.', '.', 4, 5, '.', '.', 6],
      ['.', '.', '.', '.', 2, '.', '.', '.', '.'],
      ['.', 3, 6, '.', '.', '.', 4, 1, '.'],
      [5, '.', '.', '.', '.', '.', 8, '.', 9],
      ['.', '.', '.', '.', '.', '.', '.', '.', 4],
      ['.', '.', '.', '.', 1, 8, '.', '.', '.'],
      ['.', 8, 1, 5, '.', '.', '.', 3, 2]], True),
    ([[1, 1, 1, 1, 1, 1, 1, 1, 1],
      [2, 2, 2, 2, 2, 2, 2, 2, 2],
      [3, 3, 3, 3, 3, 3, 3, 3, 3],
      [4, 4, 4, 4, 4, 4, 4, 4, 4],
      [5, 5, 5, 5, 5, 5, 5, 5, 5],
      [6, 6, 6, 6, 6, 6, 6, 6, 6],
      [7, 7, 7, 7, 7, 7, 7, 7, 7],
      [8, 8, 8, 8, 8, 8, 8, 8, 8],
      [9, 9, 9, 9, 9, 9, 9, 9, 9]], False)]
for (sudoku, expected) in sudoku_list:
    if print_sudoku:
        print 'for the sudoku:'
        print sudoku
    else:
        print 'for the next example:'
    if sol.isValidSudoku(sudoku) == expected:
        print 'my system finds the correct answer'
    else:
        print 'my system finds the incorrect answer'
