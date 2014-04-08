"""
Given an array of integers, find two numbers such that they add up to a
specific target number.
The function twoSum should return indices of the two numbers such that
they add up to the target, where index1 must be less than index2. Please 
note that your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution.
Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
Problem found here:
http://oj.leetcode.com/problems/two-sum/
"""


"""
The initial solution I wrote.  It is very slow, O(n^2), but it works
"""
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        for i in xrange(len(num)-1):
            find = target - num[i]
            for j in xrange(i+1,len(num)):
                if num[j] == find:
                    return (i,j)
        return None

    
"""
The second solution I wrote which is much quicker ( O(n) )
"""
class Solution2:
    def twoSum(self, num, target):
        index = {}
        for i in xrange(len(num)):
            if num[i] in index:
                return (index[num[i]]+1, i+1)
            else:
                index[target-num[i]] = i
        return None

#test
sol = Solution2()
values = range(10)
target = 17
print 'for list:', values
print 'and sum:', target
print 'our system finds the indices of the two numbers which add',
print 'up to the sum are',
print sol.twoSum(values, target)
