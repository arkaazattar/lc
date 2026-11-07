# Last updated: 11/7/2026, 10:34:09 AM
class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        median = nums[n // 2]
        rsp = 0

        for i in range(n):
            rsp += abs(nums[i] - median)
        
        return rsp