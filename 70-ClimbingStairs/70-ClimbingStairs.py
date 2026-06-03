# Last updated: 6/3/2026, 1:37:13 PM
1class Solution:
2    def climbStairs(self, n: int) -> int:
3        one_step, two_step = 1, 1
4        for _ in range(n - 1):
5            temp = one_step
6            one_step = one_step + two_step
7            two_step = temp
8        
9        return one_step