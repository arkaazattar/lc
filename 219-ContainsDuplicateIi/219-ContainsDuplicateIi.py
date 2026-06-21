# Last updated: 6/20/2026, 9:32:22 PM
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash = {} # num, index

        for i in range(len(nums)):
            
            if nums[i] in hash and i - hash[nums[i]] <= k:
                return True

            hash[nums[i]] = i

        return False