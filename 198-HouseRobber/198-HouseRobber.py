# Last updated: 9/29/2026, 11:25:42 AM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        """
4        at each house two options => rob, or don't rob
5        if you rob the house, you cannot rob the house after it
6
7        nums = [5, 1, 1, 5]
8        
9        dp = [5, 1, 0, 0]
10        dp = [5, 1, 6, 10]
11
12        dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
13
14        return 10
15
16        """
17        
18        if len(nums) == 1:
19            return nums[0]
20
21        dp = [0] * len(nums)
22
23        for i in range(len(nums)):
24            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
25
26        return dp[-1]