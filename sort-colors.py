"""
Given an array with n objects colored red, white or blue, sort them so
that objects of the same color are adjacent, with the colors in the
order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red,
white, and blue respectively.
Problem found here:
http://oj.leetcode.com/problems/sort-colors/
"""


"""
First solution I wrote which was accepted
"""
class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        if len(A) <= 1:
            return A
        i = 0
        for count in xrange(len(A)):
            if A[i] == 0:
                A[:] = [A[i]] + A[0:i] + A[i+1:len(A)]
            elif A[i] == 2:
                A[:] = A[0:i] + A[i+1:len(A)] + [A[i]]
                i -= 1
            i += 1

"""
A second solution which I wrote because the lines re-assigning A when a
0 or 2 were found looked clunky to me visually.
This solution also passes
"""
class Solution2:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        if len(A) <= 1:
            return A
        i = 0
        for count in xrange(len(A)):
            if A[i] == 0:
                del A[i]
                A.insert(0,0)
            elif A[i] == 2:
                del A[i]
                A.append(2)
                i -= 1
            i += 1



#test
sol = Solution()
x = [1,0]
sol.sortColors(x)
print 'we expected that this should be a sorted list: ', x
y = [1,2,0,1,1,2,2,0]
sol.sortColors(y)
print 'we expected that this should be a sorted list: ', y
