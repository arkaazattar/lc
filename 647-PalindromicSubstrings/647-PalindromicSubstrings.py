# Last updated: 10/31/2026, 6:29:03 PM
class Solution:
    def countSubstrings(self, s: str) -> int:
        palindromes = 0
    
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                palindromes += 1
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                palindromes += 1
                l -= 1
                r += 1

        return palindromes