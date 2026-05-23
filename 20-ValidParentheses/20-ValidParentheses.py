# Last updated: 5/23/2026, 2:33:49 PM
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {
            "{" : "}",
            "[" : "]",
            "(" : ")"
        }

        for char in s:
            if len(stack) == 0:
                if char in ["]", "}", ")"]:
                    return False
                stack.append(char)
            
            elif char in ["[", "{", "("]:
                stack.append(char)
            
            elif char != pair[stack.pop()]:
                return False
        
        return len(stack) == 0