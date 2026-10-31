# Last updated: 10/31/2026, 6:29:29 PM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        i, j = 0, len(numbers) - 1

        while i < j:
            if numbers[j] + numbers[i] == target:
                return [i + 1, j + 1]
            
            if numbers[j] + numbers[i] > target:
                j -= 1
            else: i += 1