# Last updated: 5/23/2026, 2:33:31 PM
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        index = 0
        for char in t:
            if index < len(s) and char == s[index]:
                index += 1

        if index == len(s):
            return True
        return False