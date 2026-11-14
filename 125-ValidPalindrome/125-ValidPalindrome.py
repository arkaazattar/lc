# Last updated: 11/13/2026, 10:28:53 PM
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        l = 0
4        r = len(s) - 1
5        s = s.lower()
6        while l < r:
7            while l < r and (not s[l].isalnum() or not s[r].isalnum()):
8                if not s[l].isalnum():
9                    l += 1
10                if not s[r].isalnum():
11                    r -= 1
12            if l < r and s[l] != s[r]:
13                return False
14            l += 1
15            r -= 1
16        return True 
17