# Last updated: 10/31/2026, 6:28:54 PM
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        rsp = [0] * n
        l = -1
        for i in range(n):
            if nums[i] < 0:
                l = i
            else:
                break
        r = l + 1

        for i in range(n):
            if r >= n:
                rsp[i] = nums[l] ** 2
                l -= 1 
            elif l < 0:
                rsp[i] = nums[r] ** 2
                r += 1
            elif abs(nums[l]) <= nums[r]:
                rsp[i] = nums[l] ** 2
                l -= 1
            else:
                rsp[i] = nums[r] ** 2
                r += 1
        
        return rsp
        
        