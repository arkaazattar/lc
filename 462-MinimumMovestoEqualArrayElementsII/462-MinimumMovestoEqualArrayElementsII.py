# Last updated: 11/2/2026, 2:53:46 PM
1class Solution:
2    def minMoves2(self, nums: list[int]) -> int:
3        n = len(nums)
4        nums.sort()
5        median = nums[n // 2]
6        rsp = 0
7
8        for i in range(n):
9            rsp += abs(nums[i] - median)
10        
11        return rsp