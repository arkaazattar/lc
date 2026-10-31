# Last updated: 10/31/2026, 6:29:21 PM
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        n = len(nums)
        cur = 0
        rsp = float("inf")
        
        while r < n:
            cur += nums[r]

            while cur >= target:
                rsp = min(rsp, r - l + 1)
                cur -= nums[l]
                l += 1
            
            r += 1
        
        if rsp == float("inf"):
            return 0
        return rsp