# Last updated: 5/23/2026, 2:33:39 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 1
        res = nums[0]
        
        for n in range(1, len(nums)):
            if nums[n] == res:
                counter += 1
            else:
                counter -= 1
            
            if counter == 0:
                res = nums[n]
                counter += 1 

        return res

