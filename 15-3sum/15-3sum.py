# Last updated: 10/31/2026, 6:29:55 PM
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        rsp = []

        for i, val in enumerate(nums):
            if i > 0 and val == nums[i - 1]:
                continue
            
            if val > 0:
                break
            
            l, r = i + 1, len(nums) - 1

            while l < r:
                total = val + nums[l] + nums[r]
                
                if total > 0:
                    r -= 1
                
                elif total < 0:
                    l += 1
                
                else:
                    rsp.append([val, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return rsp