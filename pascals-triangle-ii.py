"""
Given an index k, return the kth row of the Pascal's triangle.
For example, given k = 3, return [1,3,3,1].
Note:
Could you optimize your algorithm to use only O(k) extra space?
Problem found here:
http://oj.leetcode.com/problems/pascals-triangle-ii/
"""



class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        current_row = [1]
        cur_index = 0
        while cur_index != rowIndex:
            next_row = [1]*(len(current_row)+1)
            for i in xrange(1,len(next_row)-1):
                next_row[i] = current_row[i-1] + current_row[i]
            current_row = next_row
            cur_index += 1
        return current_row

#test
sol = Solution()
k = 5
print 'the ', 5,'row of pascals triangle found is:'
print sol.getRow(k)
