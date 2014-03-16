"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.
Leetcode problem which can be found here:
http://oj.leetcode.com/problems/jump-game/
"""



class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        jump = 1
        for i in xrange(len(A)):
            jump = jump -1
            if A[i] > jump:
                jump = A[i]
            if jump <= 0 and i != len(A)-1:
                return False
        return True


#test
sol = Solution()
do_able = range(1,10)
not_do_able = range(10,-2,-1)
print 'expected true on first example, returned: ', sol.canJump(do_able)
print 'expected false on second example, returned: ', sol.canJump(not_do_able)
