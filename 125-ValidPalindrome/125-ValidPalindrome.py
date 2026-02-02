# Last updated: 2/1/2026, 11:51:24 PM
1class Solution:
2    def isSubsequence(self, s: str, t: str) -> bool:
3        if not s:
4            return True
5        index = 0
6        for char in t:
7            if index < len(s) and char == s[index]:
8                index += 1
9
10        if index == len(s):
11            return True
12        return False