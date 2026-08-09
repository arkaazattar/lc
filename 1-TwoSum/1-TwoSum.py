# Last updated: 8/9/2026, 10:54:58 AM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        hash_map = {
4            #num : index
5        }
6
7        for i, j in enumerate(nums):
8            search_val = target - j
9            
10            if search_val in hash_map:
11                return [i, hash_map[search_val]]
12            
13            hash_map[j] = i
14        
15        return False
16