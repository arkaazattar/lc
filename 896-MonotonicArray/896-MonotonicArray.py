class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True
        
        increasing = False if nums[0] > nums[-1] else True

        for i in range(1, len(nums)):
            if increasing and nums[i] >= nums[i - 1]:
                pass
            elif not increasing and nums[i] <= nums[i - 1]:
                pass
            else:
                return False
        return True
