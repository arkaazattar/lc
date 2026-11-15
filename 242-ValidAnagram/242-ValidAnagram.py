# Last updated: 11/14/2026, 9:17:20 PM
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        if len(s) != len(t):
4            return False
5        
6        count = {}
7        for i in range(len(s)):
8            count[s[i]] = count.get(s[i], 0) + 1 
9            count[t[i]] = count.get(t[i], 0) - 1
10        
11        for val in count.values():
12            if val != 0:
13                return False
14        return True