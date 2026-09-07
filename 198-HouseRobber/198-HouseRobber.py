# Last updated: 9/7/2026, 4:23:00 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        if len(nums) == 1:
4            return nums[0]
5
6        prev1, prev2 = max(nums[0], nums[1]), nums[0] 
7
8        for i in range(2, len(nums)):
9            cur = max(prev1, prev2 + nums[i])
10            prev2 = prev1
11            prev1 = cur
12
13        return prev1