# Last updated: 9/15/2026, 11:20:00 AM
1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        nums.sort()
4        rsp = []
5
6        for i, val in enumerate(nums):
7            if i > 0 and val == nums[i - 1]:
8                continue
9            
10            if val > 0:
11                break
12            
13            l, r = i + 1, len(nums) - 1
14
15            while l < r:
16                total = val + nums[l] + nums[r]
17                
18                if total > 0:
19                    r -= 1
20                
21                elif total < 0:
22                    l += 1
23                
24                else:
25                    rsp.append([val, nums[l], nums[r]])
26                    l += 1
27                    while nums[l] == nums[l - 1] and l < r:
28                        l += 1
29        return rsp