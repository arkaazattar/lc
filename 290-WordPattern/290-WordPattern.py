# Last updated: 5/23/2026, 2:33:31 PM
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        pattern_hash = {}
        s_hash = {}
        j = 0

        if len(s) != len(pattern):
            return False

        for word in s:
            
            if pattern[j] in pattern_hash and pattern_hash[pattern[j]] != word:
                return False
            
            if word in s_hash and s_hash[word] != pattern[j]:
                return False

            pattern_hash[pattern[j]] = word
            s_hash[word] = pattern[j]
            j += 1
            
        return True