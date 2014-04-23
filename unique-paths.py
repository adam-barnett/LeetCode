"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in
the diagram below).
The robot can only move either down or right at any point in time. The robot
is trying to reach the bottom-right corner of the grid (marked 'Finish' in
the diagram below).
How many possible unique paths are there?
Note: m and n will be at most 100.
Problem found here:
http://oj.leetcode.com/problems/unique-paths/
"""



"""
creates an m by n list of lists in memory, otherwise it is almost identical
to my solution to the minimum-path-sum problem
"""
class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        if m == 0 or n == 0:
            return 0
        paths = [[0]*m for i in xrange(n)]
        for x in xrange(m):
            paths[0][x] = 1
        for y in xrange(n):
            paths[y][0] = 1
        for x in xrange(1,m):
            for y in xrange(1,n):
                paths[y][x] = paths[y-1][x] + paths[y][x-1]
        return paths[-1][-1]

#test
sol = Solution()
problems = [(1,8,1),(3,8,36),(8,3,36),(9,9,12870)]
for m,n,ans in problems:
    print 'for m and n are:', m,',',n, 'the answer is', ans
    print 'my method gives the solution:', sol.uniquePaths(m,n)
