# Last updated: 8/16/2026, 5:25:21 PM
1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3
4        i, j = 0, len(numbers) - 1
5
6        while i < j:
7            if numbers[j] + numbers[i] == target:
8                return [i + 1, j + 1]
9            
10            if numbers[j] + numbers[i] > target:
11                j -= 1
12            else: i += 1