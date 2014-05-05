"""
Say you have an array for which the ith element is the price of a given
stock on day i.
If you were only permitted to complete at most one transaction (ie, buy
one and sell one share of the stock), design an algorithm to find the
maximum profit.
Problem found here:
http://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        min_so_far = prices[0]
        max_profit = prices[1] - min_so_far
        for ind in xrange(1,len(prices)):
            min_so_far = min(min_so_far, prices[ind])
            max_profit = max(max_profit, prices[ind] - min_so_far)
        return max_profit


#test
sol = Solution()
print 'solution expected is 6'
print 'solution given is: ', sol.maxProfit([6,1,3,2,4,7])
print 'solution expected is 10'
print 'solution given is: ', sol.maxProfit([0,0,0,10,0,0])
print 'solution expected is 0'
print 'solution given is: ', sol.maxProfit([1])
print 'solution expected is 0'
print 'solution given is: ', sol.maxProfit([10,0,0,0])

