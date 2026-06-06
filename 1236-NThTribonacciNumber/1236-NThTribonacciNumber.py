# Last updated: 6/6/2026, 5:30:00 PM
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        
        dp = [0] * (n + 1) + [0]
        dp[-2], dp[-3] = 0, 1

        for i in range(len(dp) - 4, -1, -1):
            dp[i] = dp[i + 1] + dp[i + 2] + dp[i + 3]

        return dp[0]