# Last updated: 10/31/2026, 6:29:15 PM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected = 0
        for i in range(len(nums) + 1):
            expected += i
        
        for num in nums:
            expected -= num
        
        return expected
        

