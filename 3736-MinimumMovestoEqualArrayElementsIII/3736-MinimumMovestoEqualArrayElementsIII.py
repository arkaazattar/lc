# Last updated: 11/2/2026, 7:26:52 PM
1class Solution:
2    def minMoves(self, nums: List[int]) -> int:
3        highest = max(nums)
4        rsp = 0 
5
6        for num in nums:
7            rsp += highest - num
8
9        return rsp