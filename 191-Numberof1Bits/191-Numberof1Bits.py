# Last updated: 11/2/2026, 8:10:13 PM
1class Solution:
2    def hammingWeight(self, n: int) -> int:
3        ct = 0
4        for ch in str(bin(n)):
5            if ch == "1":
6                ct += 1
7
8        return ct