# Last updated: 9/17/2026, 11:15:57 AM
1class Solution:
2    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
3        rsp = 0
4        cur = 0
5
6        for num in nums:
7            if num == 1:
8                cur += 1
9            
10            else:
11                rsp = max(cur, rsp)
12                cur = 0
13        
14        return max(cur, rsp)
15