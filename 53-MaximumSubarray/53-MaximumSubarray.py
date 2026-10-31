# Last updated: 10/31/2026, 6:29:47 PM
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """
        at each num two options => create a new subarray, keep adding to prev subarray

        nums = [-2,1,-3,4,-1,2,1,-5,4]
        output = 6
        
        dp[i] = max(nums[i], nums[i] + dp[i - 1])
        
        """
        prev = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):    
            prev = max(nums[i], nums[i] + prev)
            max_sum = max(max_sum, prev) 

        return max_sum
