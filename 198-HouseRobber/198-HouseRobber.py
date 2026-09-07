# Last updated: 9/7/2026, 2:17:03 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        if len(nums) == 1:
4            return nums[0]
5
6        best = [0] * len(nums)
7
8        best[0], best[1] = nums[0], max(nums[0], nums[1])
9
10        for i in range(2, len(nums)):
11            best[i] = max(best[i - 2] + nums[i], best[i - 1])
12
13        return best[-1]