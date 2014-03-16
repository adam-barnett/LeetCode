"""
given an array A of integers every element appears twice except one,
find that one.  Leetcode problem which can be found here:
http://oj.leetcode.com/problems/single-number/
"""


class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        for index in xrange(1,len(A)):
            A[0] = A[0] ^ A[index]
        return A[0]


#testing
sol = Solution()
n = 10
A = range(5) * 2 + [n]
print 'expected value was: ', n
print 'found value was: ', sol.singleNumber(A)
