# Last updated: 10/31/2026, 9:15:14 PM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        rsp = []
4        seen = {}
5
6        for s in strs:
7            count = [0] * 26
8            for ch in s:
9                count[ord(ch) - ord('a')] += 1
10
11            count = tuple(count)
12            if count not in seen:
13                seen[count] = [s]
14            else:
15                seen[count].append(s)
16
17        for key in seen:
18            rsp.append(seen[key])
19        return rsp