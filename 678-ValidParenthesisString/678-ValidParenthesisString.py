# Last updated: 8/13/2026, 7:06:52 PM
1class Solution:
2    def checkValidString(self, s: str) -> bool:
3        
4        min_left, max_left = 0, 0
5
6        for char in s:
7            if char == '(':
8                min_left, max_left = min_left + 1, max_left + 1
9
10            elif char == ')':
11                min_left, max_left = min_left - 1, max_left - 1
12            
13            else:
14                min_left, max_left = min_left - 1, max_left + 1
15            
16            if max_left < 0:
17                return False
18            
19            if min_left < 0:
20                min_left = 0
21            
22        return min_left == 0
23