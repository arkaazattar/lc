# Last updated: 11/3/2026, 12:42:32 AM
1class Solution:
2    def hammingWeight(self, n: int) -> int:
3        ct = 0
4
5        while n:
6            ct += n & 1
7            n >>= 1
8
9        return ct