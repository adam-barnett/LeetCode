"""
Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:
- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.
For example,
Consider the following matrix:
[[1, 3, 5, 7],
 [10, 11, 16, 20],
 [23, 30, 34, 50]]
Given target = 3, return true.
Problem found here:
http://oj.leetcode.com/problems/search-a-2d-matrix/
"""


class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0:
            return False
        for row in matrix:
            if len(row) == 0:
                return False
            if row[-1] >= target:
                return self.binarySearch(row, target)
        return False
        
    def binarySearch(self, values, target):
        lower = 0
        upper = len(values)
        while lower != upper:
            half_way = lower + (upper - lower)/2
            if values[half_way] == target:
                return True
            elif values[half_way] > target:
                upper = half_way
            else:
                lower = half_way + 1
        return False

#test
sol = Solution()
tests = [(1, [[1]]), (2, [[1]]), (1, [[]]), (5, [[1,2,3],[4,5,6],[7,8,9]])]
for (val, mat) in tests:
    print 'my system says that it is', sol.searchMatrix(mat, val)
    print 'that the value', val, 'is in the matrix', mat, '\n\n'
