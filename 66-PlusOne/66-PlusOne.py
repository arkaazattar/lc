# Last updated: 8/13/2026, 2:53:50 PM
1class Solution:
2    def plusOne(self, digits: List[int]) -> List[int]:
3        
4        digits[-1] += 1
5        for i in range(len(digits) -1, -1, -1):
6            # condition that there is a carry
7            if digits[i] == 10:
8                digits[i] = 0
9                
10                if i != 0:
11                    digits[i - 1] += 1
12                
13                else:
14                    digits = [1] + digits
15
16            else:
17                return digits
18        
19        return digits
20