# Last updated: 11/1/2026, 1:50:28 PM
1class Solution:
2    def maxSubArray(self, nums: list[int]) -> int:
3        """
4        at each element you have two options, continue previous subarray or start new
5
6        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
7        output = 6
8
9        dp = [-2, 1, -2, 4, 3, 5, 6, 1, 5]
10
11        """
12        dp = [0] * len(nums)
13        dp[0] = nums[0]
14        rsp = dp[0]
15
16        for i in range(1, len(nums)):
17            dp[i] = max(nums[i], dp[i - 1] + nums[i])
18            rsp = max(rsp, dp[i])
19        
20        return rsp