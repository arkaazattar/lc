# Last updated: 5/20/2026, 5:44:36 PM
1class Solution:
2    def isIsomorphic(self, s: str, t: str) -> bool:
3        s_hash = {}
4        t_hash = {}
5
6        for i in range(len(s)):
7            s_char = s[i]
8            t_char = t[i]
9
10            if((s_char in s_hash and s_hash[s_char] != t_char) or 
11                (t_char in t_hash and t_hash[t_char] != s_char)):
12                return False
13
14            s_hash[s_char] = t_char
15            t_hash[t_char] = s_char
16        
17        return True