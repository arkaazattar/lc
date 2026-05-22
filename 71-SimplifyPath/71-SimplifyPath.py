# Last updated: 5/22/2026, 2:26:21 PM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        stack = []
4        pair = {
5            "{" : "}",
6            "[" : "]",
7            "(" : ")"
8        }
9
10        for char in s:
11            if len(stack) == 0:
12                if char in ["]", "}", ")"]:
13                    return False
14                stack.append(char)
15            
16            elif char in ["[", "{", "("]:
17                stack.append(char)
18            
19            elif char != pair[stack.pop()]:
20                return False
21        
22        return len(stack) == 0