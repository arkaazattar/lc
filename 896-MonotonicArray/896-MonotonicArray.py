class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True
        
        increasing = True if nums[0] <= nums[-1] else False
        
        i, j = 0, 1

        if increasing:
            while j < len(nums):
                if nums[i] > nums[j]:
                    return False
                i += 1
                j += 1
            return True

        else:
            while j < len(nums):
                if nums[i] < nums[j]:
                    return False
                i += 1
                j += 1
            return True
