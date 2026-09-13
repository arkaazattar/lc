# Last updated: 9/13/2026, 3:16:31 PM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        res = ""
4        res_len = 0
5        
6        for i in range(len(s)):
7            
8            l, r = i, i + 1
9            while l >= 0 and r < len(s) and s[l] == s[r]:
10                    if r - l + 1 > res_len:
11                        res = s[l : r + 1]
12                        res_len = r - l + 1
13                    l -= 1
14                    r += 1
15
16            l, r = i, i
17            while l >= 0 and r < len(s) and s[l] == s[r]:
18                if r - l + 1 > res_len:
19                    res = s[l : r + 1]
20                    res_len = r - l + 1
21                l -= 1
22                r += 1
23
24        return res