# Last updated: 5/14/2026, 4:56:03 PM
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        k = 1
        j = 1

        while j < len(nums):
            if nums[j] != nums[k - 1]:
                nums[k] = nums[j]
                k += 1
            j += 1
        return k    

        