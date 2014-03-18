"""
Given numRows, generate the first numRows of Pascal's triangle.
Problem can be found here:
http://oj.leetcode.com/problems/pascals-triangle/
"""



class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        pascal = []
        if numRows == 0:
            return pascal
        pascal.append([1])
        numRows -= 1
        while numRows > 0:
            next_row = [1]*(len(pascal[-1])+1)
            for i in xrange(1,len(next_row)-1):
                next_row[i] = pascal[-1][i-1] + pascal[-1][i]
            pascal.append(next_row)
            numRows -= 1
        return pascal


#test
sol = Solution()
numRows = 5
triangle = sol.generate(numRows)
for row in triangle:
    print row
