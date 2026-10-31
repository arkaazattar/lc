# Last updated: 10/31/2026, 6:29:30 PM
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        """
        nums = [1, 2, 1, 3, 5, 6, 4]

        output = 1 (2) or 5 (6)

        reason: 2 and 6 are the local maxes

        nums - [1, 2, 3, 4, 5, 6, 7, 8, 9, 1] n = 10 lo = 0 hi = 9
        output = 8

        """
        low, high = 0, len(nums) - 1
        nums.append(float("-inf"))

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] < nums[mid + 1]:
                low = mid + 1
            else:
                high = mid - 1
            
        return low


