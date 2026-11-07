# Last updated: 11/7/2026, 10:34:15 AM
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for n, c in count.items():
            freq[c].append(n)
        
        rsp = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                rsp.append(n)
                if len(rsp) == k:
                    return rsp

 
