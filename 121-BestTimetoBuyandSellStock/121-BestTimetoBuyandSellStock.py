# Last updated: 1/15/2026, 2:00:21 AM
1class Solution(object):
2    def maxProfit(self, prices):
3        """
4        :type prices: List[int]
5        :rtype: int
6        """
7        cur = 0
8        maxprofit = 0
9        for nxt in range(1, len(prices)):
10            if prices[nxt] - prices[cur] > 0:
11                profit = prices[nxt] - prices[cur]
12                maxprofit = max(profit, maxprofit) 
13            else:
14                cur = nxt
15        return maxprofit
16
17