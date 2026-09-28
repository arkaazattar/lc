# Last updated: 9/28/2026, 2:42:11 PM
1class Solution:
2    def minCostClimbingStairs(self, cost: List[int]) -> int:
3        # dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
4        # if len(cost) == 2:
5        #     return min(cost[0], cost[1])
6
7        # dp = [0] * len(cost)
8        # dp[-1], dp[-2] = cost[-1], cost[-2]
9
10        # for i in range(len(cost) -3, -1, -1):
11        #     dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
12
13        # return min(dp[0], dp[1])
14
15        cost.append(0)
16        for i in range(len(cost) - 3, -1, -1):
17            cost[i] = cost[i] + min(cost[i + 1], cost[i + 2])
18
19        return min(cost[0], cost[1])