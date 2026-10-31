# Last updated: 10/31/2026, 6:29:41 PM
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 1        

        i = 1
        ct = 1
        while i < len(nums):
            if nums[i] == nums[i - 1] and ct == 2:
                nums.pop(i)
                i -= 1
            
            elif nums[i] == nums[i - 1]:
                ct += 1

            else:
                ct = 1

            i +=1

        return len(nums)