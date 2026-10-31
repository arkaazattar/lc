# Last updated: 10/31/2026, 6:29:20 PM
class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        at each index two options => rob, don't rob
        condition to rob, adjacent house has not been robbed and the list is a loop

        nums = [2, 3, 2]
        
        break into two dp problems and find the max:
            go from 0:n -1 and from 1:n

        index 0 and -1 are considered adjacent

        """
        if len(nums) == 1:
            return nums[0]

        elif len(nums) == 2:
            return max(nums)

        dp1 = [0] * (len(nums) - 1)
        dp2 = [0] * (len(nums) - 1)
        
        for i in range(len(nums) - 1):
            dp1[i] = max(nums[i] + dp1[i - 2], dp1[i - 1])
        
        for i in range(1, len(nums)):
            dp2[i - 1] = max(nums[i] + dp2[i - 3], dp2[i - 2])

        return max(dp1[-1], dp2[-1])
        