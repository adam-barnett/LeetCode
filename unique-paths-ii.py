"""
Follow up for "Unique Paths":
Now consider if some obstacles are added to the grids. How many unique
paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.
For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.
[[0,0,0],
 [0,1,0],
 [0,0,0]]
The total number of unique paths is 2.
Note: m and n will be at most 100.
Problem found here:
http://oj.leetcode.com/problems/unique-paths-ii/
"""


"""
I solve the problem in place on the input grid, switching all of the values
of the obstacles from 1 to -1 so they can be appropriately ignored.
"""
class Solution:
    # @param grid_obs, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, grid_obs):
        if not grid_obs or not grid_obs[0]:
            return 0
        if grid_obs[0][0] == 1:
            return 0
        for i in xrange(len(grid_obs)):
            for j in xrange(len(grid_obs[i])):
                if i == 0 and j == 0:
                    grid_obs[i][j] = 1
                elif grid_obs[i][j] == 1:
                    grid_obs[i][j] = -1
                else:
                    if i:
                        grid_obs[i][j] += max(grid_obs[i-1][j], 0)
                    if j:
                        grid_obs[i][j] += max(grid_obs[i][j-1], 0)
        return max(grid_obs[-1][-1], 0)

#test
sol = Solution()
test_cases = [
    ([[0]],1),
    ([[1]],0),
    ([[0,1]],0),
    ([[0,0,0],[0,1,0],[0,0,0]],2)]
for (case, expected) in test_cases:
    print '\nFor the grid:', case, ' there are:', expected, 'routes'
    print 'our system finds:', sol.uniquePathsWithObstacles(case),
    print 'routes'
    
