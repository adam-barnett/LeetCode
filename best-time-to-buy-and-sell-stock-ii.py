"""
Say you have an array for which the ith element is the price of a given
stock on day i.
Design an algorithm to find the maximum profit. You may complete as many
transactions as you like (ie, buy one and sell one share of the stock
multiple times). However, you may not engage in multiple transactions at
the same time (ie, you must sell the stock before you buy again).
Problem found here:
http://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
"""



"""
Note. This solution could have been more succinct but I specifically
set out to challenge myself to maximise the profits while carrying 
out the minimum number of transactions (that is, not simply 
buying/selling whenever prices[i] < prices[i+1]).
"""
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        current_min = prices[0]
        total_profit = 0
        for ind in xrange(1,len(prices)):
            if prices[ind] < prices[ind-1]:
                total_profit += prices[ind-1] - current_min
                current_min = prices[ind]
            else:
                current_min = min(current_min, prices[ind])
        if prices[-1] >= prices[-2] and prices[-1] > current_min:
            total_profit += prices[-1] - current_min
        return total_profit


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

