# Last updated: 5/14/2026, 4:56:04 PM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        rsp = ""

        for i in range(len(strs[0])):
            for string in strs:
                if i == len(string) or string[i] != strs[0][i]:
                    return rsp
            rsp += strs[0][i]
        
        return rsp