"""
Given a m x n matrix, if an element is 0, set its entire row and column
to 0. Do it in place. 
Problem found here:
http://oj.leetcode.com/problems/set-matrix-zeroes/
"""

import random


class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        top_is_zero = False
        left_is_zero = False
        for i in matrix[0]:
            if i == 0:
                top_is_zero = True
                break
        for i in matrix:
            if i[0] == 0:
                left_is_zero = True
                break
        for x in xrange(1,len(matrix[0])):
            for y in xrange(1,len(matrix)):
                if matrix[y][x] == 0:
                    matrix[y][0] = 0
                    matrix[0][x] = 0
        for x in xrange(1, len(matrix[0])):
            if matrix[0][x] == 0:
                for y in xrange(1,len(matrix)):
                    matrix[y][x] = 0
        for y in xrange(1, len(matrix)):
            if matrix[y][0] == 0:
                for x in xrange(1, len(matrix[0])):
                    matrix[y][x] = 0
        if top_is_zero:
            matrix[0] = [0]*len(matrix[0])
        if left_is_zero:
            for y in matrix:
                y[0] = 0
#test
sol = Solution()
size = 12
zero_prob = 30
choices = [1]*zero_prob + [0]
matrix = []
for i in xrange(size):
    matrix.append([random.choice(choices) for r in xrange(size)])
print 'original matrix is:'
for i in matrix:
    print i
sol.setZeroes(matrix)
print '\n after setting the zeroes the matrix is:'
for i in matrix:
    print i
