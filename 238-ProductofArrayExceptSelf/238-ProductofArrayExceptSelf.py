# Last updated: 3/19/2026, 6:08:14 PM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        
4        ans = [1] * len(nums)
5        left = 1
6        right = 1
7
8        for i in range(len(nums)):
9            ans[i] = left
10            left = left * nums[i]
11        for i in range(len(nums) - 1, -1, -1):
12            ans[i] *= right
13            right = right * nums[i]
14        
15        return ans