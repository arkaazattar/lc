# Last updated: 9/13/2026, 5:14:03 PM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        max_area = 0
4        
5        l, r = 0, len(height) - 1
6        while l < r:
7            if height[l] < height[r]:
8                max_area = max(max_area, min(height[l], height[r]) * (r - l))
9                l += 1
10            
11            else:
12                max_area = max(max_area, min(height[l], height[r]) * (r - l))
13                r -= 1
14
15        return max_area