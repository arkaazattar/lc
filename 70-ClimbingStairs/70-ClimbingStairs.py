# Last updated: 9/27/2026, 3:45:43 PM
1class Solution:
2    def climbStairs(self, n: int) -> int:
3        """
4        n = 1 => 1
5        n = 2 => 2
6        n = 3 => 3
7        n = 4 => 5
8        n = 5 => 8
9        n = 6 => 13
10        """
11        if n == 1:
12            return 1
13            
14        dp = [0] * n
15        dp[0], dp[1] = 1, 2
16
17        for i in range(2, n):
18            dp[i] = dp[i - 1] + dp[i - 2] 
19
20        return dp[-1]
21