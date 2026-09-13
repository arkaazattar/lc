# Last updated: 9/13/2026, 3:16:20 PM
1class Solution:
2    def missingNumber(self, nums: List[int]) -> int:
3        expected = 0
4        for i in range(len(nums) + 1):
5            expected += i
6        
7        for num in nums:
8            expected -= num
9        
10        return expected
11        
12
13