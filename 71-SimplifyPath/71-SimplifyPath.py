# Last updated: 5/23/2026, 2:33:44 PM
class Solution:
    def simplifyPath(self, path: str) -> str:
        simplified_path = "/"
        stack = []
        
        curr = ""
        if path[len(path) - 1] != '/':
            path += '/'
        for char in path:
            if char == "/":
                if curr == "":
                    continue
                elif curr == '.':
                    curr = ""
                    continue

                if stack and curr == "..":
                    stack.pop() 
                    curr = ""
                    continue
                elif not stack and curr == "..":
                    curr = ""
                    continue

                stack.append(curr)
                curr = ""

            else:
                curr += char

        for i in range(len(stack)):
            simplified_path += stack[i]

            if i != len(stack) - 1:
                simplified_path += '/'
            
        return simplified_path
        
