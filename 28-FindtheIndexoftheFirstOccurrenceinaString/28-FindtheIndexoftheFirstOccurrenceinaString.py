# Last updated: 5/19/2026, 6:38:44 PM
1class Solution:
2    def removeElement(self, nums: List[int], val: int) -> int:
3        i = 0
4        j = len(nums)
5
6        while i < j:
7            if nums[i] == val:
8                nums[i] = nums[j - 1]
9                j -= 1
10            else:
11                i += 1
12        return j
13                