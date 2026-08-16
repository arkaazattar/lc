# Last updated: 8/16/2026, 5:25:09 PM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        left, right = 0, len(height) - 1
4
5        area = 0
6
7        # move the lower height inwards
8        while left < right:
9            cur_area = min(height[left], height[right]) * (right - left)
10
11            area = max(area, cur_area)
12            
13            if height[left] < height[right]:
14                left += 1
15            
16            else:
17                right -= 1
18        
19        return area
20            