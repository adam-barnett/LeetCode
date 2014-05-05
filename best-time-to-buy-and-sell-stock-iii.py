"""
Say you have an array for which the ith element is the price of a given
stock on day i.
Design an algorithm to find the maximum profit. You may complete at most
two transactions.
Note:
You may not engage in multiple transactions at the same time (ie, you must
sell the stock before you buy again).
Problem found here:
http://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
"""

"""
max_forward keeps track of the maximum profit gathered when moving forward
through the prices, then we step backwards comparing our maximum at each
point to the maximum obtained when moving forwards.
note. this solution does not generalise to an arbitrary number of trades
"""
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        max_forward = [0]*len(prices)
        max_so_far = 0
        min_found = prices[0]
        for ind in xrange(1,len(prices)):
            min_found = min(min_found, prices[ind])
            max_so_far = max(max_so_far, prices[ind] - min_found)
            max_forward[ind] = max(max_forward[ind], max_so_far)
        max_found = prices[-1]
        max_two_trans = 0
        for ind in xrange(len(prices)-2,-1,-1):
            max_found = max(max_found, prices[ind])
            max_two_trans = max(max_two_trans,
                max_found - prices[ind] + max_forward[ind])
        return max_two_trans

#test
sol = Solution()
print 'solution expected is 7'
print 'solution given is: ', sol.maxProfit([6,1,3,2,4,7])
print 'solution expected is 10'
print 'solution given is: ', sol.maxProfit([0,0,0,10,0,0])
print 'solution expected is 0'
print 'solution given is: ', sol.maxProfit([1])
print 'solution expected is 0'
print 'solution given is: ', sol.maxProfit([10,0,0,0])

