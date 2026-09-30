# Last updated: 9/30/2026, 7:34:02 PM
1class Solution:
2    def reverseString(self, s: list[str]) -> None:
3        """
4        Do not return anything, modify s in-place instead.
5        """
6        i, j = 0, len(s) - 1
7
8        while i < j:
9            temp = s[i]
10            s[i] = s[j]
11            s[j] = temp
12
13            i += 1
14            j -= 1