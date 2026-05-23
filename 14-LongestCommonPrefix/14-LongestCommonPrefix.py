# Last updated: 5/23/2026, 2:33:50 PM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        rsp = ""

        for i in range(len(strs[0])):
            for string in strs:
                if i == len(string) or string[i] != strs[0][i]:
                    return rsp
            rsp += strs[0][i]
        
        return rsp