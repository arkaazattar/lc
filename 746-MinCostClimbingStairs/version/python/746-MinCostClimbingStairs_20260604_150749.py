# Last updated: 6/4/2026, 3:07:49 PM
1class Solution:
2    def minCostClimbingStairs(self, cost: List[int]) -> int:
3        cost.append(0)
4
5        for i in range(len(cost) - 3, -1, -1):
6            cost[i] = min(cost[i] + cost[i + 1], cost[i] + cost[i + 2])
7
8        return min(cost[0], cost[1])