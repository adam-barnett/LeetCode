"""
Given a set of distinct integers, S, return all possible subsets.
Note:
 Elements in a subset must be in non-descending order.
 The solution set must not contain duplicate subsets.
For example,
If S = [1,2,3], a solution is: [[3],[1],[2],[1,2,3],[1,3],[2,3],[1,2],[]]
Problem found here:
http://oj.leetcode.com/problems/subsets/
"""

class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        sets = [[]]
        if len(S) == 0:
            return sets
        S.sort()
        for int in S:
            sets = sets + [i + [int] for i in sets]
        return sets

#tests
sol = Solution()
tests = [[0],[1,2,3],[5,2,0],[]]
for test in tests:
    print 'for', test, 'our system returned the subsets:'
    print sol.subsets(test)
