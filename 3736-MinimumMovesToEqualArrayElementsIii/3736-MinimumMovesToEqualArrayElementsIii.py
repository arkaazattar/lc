# Last updated: 11/7/2026, 10:33:44 AM
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        highest = max(nums)
        rsp = 0 

        for num in nums:
            rsp += highest - num

        return rsp