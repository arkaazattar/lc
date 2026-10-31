# Last updated: 10/31/2026, 4:10:23 PM
1class Solution:
2    def searchInsert(self, nums: list[int], target: int) -> int:
3        low, high = 0, len(nums) - 1
4
5        while low <= high:
6            mid = low + (high - low) // 2
7
8            if nums[mid] == target:
9                return mid
10            
11            elif nums[mid] > target:
12                high = mid - 1
13            
14            else:
15                low = mid + 1
16        
17        return low