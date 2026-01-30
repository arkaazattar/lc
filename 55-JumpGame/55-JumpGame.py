# Last updated: 1/30/2026, 12:03:18 AM
1class Solution:
2    def canJump(self, nums: List[int]) -> bool:
3        if len(nums) == 1:
4            return True
5        
6        safe = len(nums) - 1
7        # start at last element
8        for i in range(len(nums) - 1, -1, -1 ):
9            if nums[i] >= safe - i:
10                safe = i
11        
12        if safe == 0:
13            return True
14        return False
15