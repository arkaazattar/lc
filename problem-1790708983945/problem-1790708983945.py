# Last updated: 9/29/2026, 3:09:43 PM
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
12        prev = nums[0]
13        max_sum = nums[0]
14
15        for i in range(1, len(nums)):    
16            prev = max(nums[i], nums[i] + prev)
17            max_sum = max(max_sum, prev) 
18
19        return max_sum
20