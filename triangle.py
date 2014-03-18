"""
Given a triangle, find the minimum path sum from top to bottom.
Each step you may move to adjacent numbers on the row below.
Problem can be found here:
http://oj.leetcode.com/problems/triangle/
"""



"""
note: by modifying the triangle in place this uses constant extra space.
However it could be problematic if the requirements also specified that
we avoided altering triangle.
"""
class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if len(triangle) == 0:
            return 0
        if len(triangle) == 1:
            return triangle[0][0]
        for depth in xrange(len(triangle)-2, -1, -1):
            for breadth in xrange(len(triangle[depth])):
                if triangle[depth+1][breadth] > triangle[depth+1][breadth+1]:
                    triangle[depth][breadth] += triangle[depth+1][breadth+1]
                else:
                    triangle[depth][breadth] += triangle[depth+1][breadth]
        return triangle[0][0]

#test
sol = Solution()
triangle = [[1],[2,3],[4,5,6],[7,8,9,1]]
print 'expected 12, returned: ', sol.minimumTotal(triangle)
