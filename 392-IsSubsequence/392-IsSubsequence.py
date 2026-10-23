# Last updated: 10/22/2026, 11:53:20 PM
1class Solution:
2    def isSubsequence(self, s: str, t: str) -> bool:
3
4        s_ptr = 0
5        
6        for i in range(len(t)):
7            if s_ptr < len(s) and s[s_ptr] == t[i]:
8                s_ptr += 1
9
10        if s_ptr != len(s):
11            return False
12
13        return True