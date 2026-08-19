# Last updated: 8/19/2026, 3:25:18 PM
1class Solution:
2    def canJump(self, nums: List[int]) -> bool:
3        goal = len(nums) - 1
4
5        for i in range(len(nums) -2, -1, -1):
6            if nums[i] >= (goal - i):
7                goal = i
8        
9        return goal == 0
10