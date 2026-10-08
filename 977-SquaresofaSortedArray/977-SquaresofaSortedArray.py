# Last updated: 10/8/2026, 2:29:46 PM
1class Solution:
2    def sortedSquares(self, nums: list[int]) -> list[int]:
3        n = len(nums)
4        rsp = [0] * n
5        l = -1
6        for i in range(n):
7            if nums[i] < 0:
8                l = i
9            else:
10                break
11        r = l + 1
12
13        for i in range(n):
14            if r >= n:
15                rsp[i] = nums[l] ** 2
16                l -= 1 
17            elif l < 0:
18                rsp[i] = nums[r] ** 2
19                r += 1
20            elif abs(nums[l]) <= nums[r]:
21                rsp[i] = nums[l] ** 2
22                l -= 1
23            else:
24                rsp[i] = nums[r] ** 2
25                r += 1
26        
27        return rsp
28        
29        