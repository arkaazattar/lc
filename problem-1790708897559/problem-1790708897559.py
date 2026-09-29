# Last updated: 9/29/2026, 3:08:17 PM
1class Solution:
2    def maxSubArray(self, nums: list[int]) -> int:
3        """
4        at each num two options => create a new subarray, keep adding to prev subarray
5
6        nums = [-2,1,-3,4,-1,2,1,-5,4]
7        output = 6
8        
9        dp[i] = max(nums[i], nums[i] + dp[i - 1])
10        
11        """
12
13        dp = [0] * len(nums)
14        dp[0] = nums[0]
15        max_sum = nums[0]
16
17        for i in range(1, len(nums)):    
18            dp[i] = max(nums[i], nums[i] + dp[i - 1])
19            max_sum = max(max_sum, dp[i]) 
20
21        return max_sum
22