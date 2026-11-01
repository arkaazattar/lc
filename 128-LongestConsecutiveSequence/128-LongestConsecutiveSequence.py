# Last updated: 11/1/2026, 2:46:38 PM
1class Solution:
2    def longestConsecutive(self, nums: list[int]) -> int:
3        nums = set(nums)
4        longest = 0
5        
6        for num in nums:
7            # start of a sequence
8            if num - 1 not in nums:
9                length = 0
10                while num + length in nums:
11                    length += 1
12                longest = max(longest, length)
13
14        return longest 