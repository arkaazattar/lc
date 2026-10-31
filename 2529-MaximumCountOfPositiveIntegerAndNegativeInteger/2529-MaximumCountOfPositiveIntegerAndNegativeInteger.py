# Last updated: 10/31/2026, 6:28:42 PM
class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        neg_count = 0
        length = len(nums)
        non_zero_length = 0

        for i in range(length):
            if nums[i] < 0:
                neg_count += 1
            elif nums[i] == 0:
                non_zero_length += 1
            else:
                break
        
        pos_count = length - neg_count - non_zero_length

        if pos_count < neg_count:
            return neg_count
        return pos_count