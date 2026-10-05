# Last updated: 10/5/2026, 3:43:28 PM
1class Solution:
2    def coinChange(self, coins: list[int], amount: int) -> int:
3        coins.sort()
4
5        dp = [float("inf")] * (amount + 1)
6        dp[0] = 0
7
8        for cur_amount in range(1, amount + 1):
9            for j in range(len(coins)):
10                if coins[j] > cur_amount:
11                    break
12                dp[cur_amount] = min(dp[cur_amount], dp[cur_amount - coins[j]] + 1)
13
14        if dp[-1] == float("inf"):
15            return -1
16        return dp[-1]
17