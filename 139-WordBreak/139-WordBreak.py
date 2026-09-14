# Last updated: 9/14/2026, 7:53:57 PM
1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
3        words = set(wordDict)
4
5        dp = [False] * (len(s) + 1)
6        dp[0] = True
7
8        for i in range(len(s)):
9            # skip positions that are False
10            if not dp[i]:
11                continue
12
13            for j in range(i + 1, len(s) + 1):
14                if s[i:j] in words:
15                    dp[j] = True
16        
17        return dp[-1]