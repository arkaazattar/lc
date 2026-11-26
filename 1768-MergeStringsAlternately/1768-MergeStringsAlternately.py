class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        rsp_arr = []
        n = max(len(word1), len(word2))
        for i in range(n):
            if i < len(word1):
                rsp_arr.append(word1[i])
            if i < len(word2):
                rsp_arr.append(word2[i])

        return "".join(rsp_arr)
