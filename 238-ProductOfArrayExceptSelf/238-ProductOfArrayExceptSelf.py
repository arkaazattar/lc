# Last updated: 5/14/2026, 4:55:56 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = [1] * len(nums)
        left = 1
        right = 1

        for i in range(len(nums)):
            ans[i] = left
            left = left * nums[i]
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= right
            right = right * nums[i]
        
        return ans