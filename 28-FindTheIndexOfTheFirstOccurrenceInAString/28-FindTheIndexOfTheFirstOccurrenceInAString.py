# Last updated: 5/22/2026, 10:32:53 PM
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle == "":
            return 0
        
        for i in range(len(haystack) - len(needle) + 1):
            j = 0

            while haystack[j + i] == needle[j]:
                j += 1
                
                if j == len(needle):
                    return i
        
        return -1

