# Last updated: 5/23/2026, 2:33:46 PM
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        safe = len(nums) - 1
        # start at last element
        for i in range(len(nums) - 1, -1, -1 ):
            if nums[i] >= safe - i:
                safe = i
        
        if safe == 0:
            return True
        return False
