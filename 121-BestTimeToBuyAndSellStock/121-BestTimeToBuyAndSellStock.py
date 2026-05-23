# Last updated: 5/23/2026, 2:29:31 PM
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cur = 0
        maxprofit = 0
        for nxt in range(1, len(prices)):
            if prices[nxt] - prices[cur] > 0:
                profit = prices[nxt] - prices[cur]
                maxprofit = max(profit, maxprofit) 
            else:
                cur = nxt
        return maxprofit

