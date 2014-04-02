"""
Given a 2D binary matrix filled with 0's and 1's, find the largest
rectangle containing all ones and return its area.
Problem found here:
http://oj.leetcode.com/problems/maximal-rectangle/
"""

#note - current solution fails as it takes too long.  Problem not fully solved.

"""
This is my initial solution, it is correct but much too slow as it checks
all possible permutations of rectangles.  Probably a much more efficient
solution will be to change the matrix in place
"""
class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if len(matrix) == 0:
            return 0
        if len(matrix[0]) == 0:
            return 0
        max_size = 0
        for y in xrange(len(matrix)):
            for x in xrange(len(matrix[y])):
                if matrix[y][x] == '1':
                    x_max = x
                    while matrix[y][x_max] == '1':
                        x_max += 1
                        y_max = self.extendDown(y, x, x_max, matrix)
                        area = (x_max - x) * (y_max - y)
                        if area > max_size:
                            max_size = area
                        if x_max == len(matrix[y]):
                            break
        return max_size
                    
                    
                    
    def extendAcross(self, y, x, matrix):
        for step in xrange(x, len(matrix[y])):
            if matrix[y][step] != '1':
                return step
        return len(matrix[y])
                
    def extendDown(self, y, x, x_max, matrix):
        for step in xrange(y,len(matrix)):
            for check in xrange(x, x_max):
                if matrix[step][check] != '1':
                    return step
        return len(matrix)


#test
sol = Solution()
print 'expected solution 12, my solution returns: '
print sol.maximalRectangle(["0010","1111","1111","1110","1100","1111","1110"])
