# Last updated: 9/10/2026, 12:07:47 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        left, right, best = 0, 0, 1
4        seen = set()
5
6        if len(s) == 0:
7            return 0
8
9        while right < len(s):
10            if s[right] not in seen:
11                seen.add(s[right])
12                right += 1
13                
14            else:
15                best = max(best, right - left)
16                seen.remove(s[left])
17                left += 1
18
19        return max(best, right - left)