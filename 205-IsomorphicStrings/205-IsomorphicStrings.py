# Last updated: 5/22/2026, 10:32:46 PM
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}

        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]

            if((s_char in s_hash and s_hash[s_char] != t_char) or 
                (t_char in t_hash and t_hash[t_char] != s_char)):
                return False

            s_hash[s_char] = t_char
            t_hash[t_char] = s_char
        
        return True