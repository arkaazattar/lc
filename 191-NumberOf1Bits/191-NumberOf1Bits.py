# Last updated: 11/7/2026, 10:34:58 AM
class Solution:
    def hammingWeight(self, n: int) -> int:
        ct = 0

        while n:
            ct += n & 1
            n >>= 1

        return ct