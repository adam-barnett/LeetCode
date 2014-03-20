"""
Given an array and a value, remove all instances of that value in place
and return the new length.
The order of elements can be changed. It doesn't matter what you leave
beyond the new length.
Problem found here:
http://oj.leetcode.com/problems/remove-element/
"""



class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        index = 0
        while index < len(A):
            if A[index] == elem:
                del A[index]
                index -= 1
            index += 1
        return len(A)


#test
sol = Solution()
x = range(10)
y = [5]*10
z = 5
print 'removing: ', z, ' from ', x
print 'our method says the new length is: ', sol.removeElement(x, z)
print 'removing: ', z, ' from ', y
print 'our method says the new length is: ', sol.removeElement(y, z)
