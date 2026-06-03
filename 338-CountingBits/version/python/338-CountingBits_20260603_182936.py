# Last updated: 6/3/2026, 6:29:36 PM
1class Solution:
2    def countBits(self, n: int) -> List[int]:
3        ans = [0] * (n + 1)
4        pos = 1
5
6        for i in range(1, n + 1):
7            if 2 * pos == i:
8                pos = i
9            ans[i] = 1 + ans[i - pos]
10
11        return ans
12