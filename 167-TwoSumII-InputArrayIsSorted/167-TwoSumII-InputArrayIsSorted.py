# Last updated: 11/10/2026, 10:41:03 PM
1class Solution:
2    def twoSum(self, numbers: list[int], target: int) -> list[int]:
3        l, r = 0, len(numbers) - 1
4
5        while l < r:
6            if numbers[l] + numbers[r] == target:
7                return [l + 1, r + 1]
8            
9            elif numbers[l] + numbers[r] > target:
10                r -= 1
11            else:
12                l += 1