"""
Given a m x n grid filled with non-negative numbers, find a path from
top left to bottom right which minimizes the sum of all numbers along
its path.
Note: You can only move either down or right at any point in time.
Problem found here:
http://oj.leetcode.com/problems/minimum-path-sum/
"""


"""
Here my solution assumes that grid can be changed in place, if grid needs
to be preserved then a separate grid would have be created
"""
class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        if len(grid) == 0:
            return 0
        for x in xrange(1,len(grid[0])):
            grid[0][x] += grid[0][x-1]
        for y in xrange(1,len(grid)):
            grid[y][0] += grid[y-1][0]
        for x in xrange(1,len(grid[0])):
            for y in xrange(1,len(grid)):
                min_route = min(grid[y-1][x], grid[y][x-1])
                grid[y][x] += min_route
        return grid[-1][-1]


#test
sol = Solution()
zero_path = ([[0]*3,[0]*3,[0]*3], 0)
five_path = ([[1]*3,[1]*3,[1]*3], 5)
ten_path = ([[2,2,4],[4,2,4],[4,2,2]], 10)
paths = []
paths.append(zero_path)
paths.append(five_path)
paths.append(ten_path)
for i in paths:
    print 'for the grid', i[0], 'expected result is', i[1]
    print 'our solution returns a path length of:',
    print sol.minPathSum(i[0])
