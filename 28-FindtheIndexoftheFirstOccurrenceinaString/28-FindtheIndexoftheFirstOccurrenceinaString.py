# Last updated: 5/19/2026, 5:25:16 PM
1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3        
4        if needle == "":
5            return 0
6        
7        for i in range(len(haystack) - len(needle) + 1):
8            j = 0
9
10            while haystack[j + i] == needle[j]:
11                j += 1
12                
13                if j == len(needle):
14                    return i
15        
16        return -1
17
18