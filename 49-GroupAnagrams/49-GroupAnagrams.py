# Last updated: 11/7/2026, 10:35:54 AM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rsp = []
        seen = {}

        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1

            count = tuple(count)
            if count not in seen:
                seen[count] = [s]
            else:
                seen[count].append(s)

        return list(seen.values())