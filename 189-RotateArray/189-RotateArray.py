# Last updated: 1/29/2026, 11:24:42 PM
1class Solution:
2    def rotate(self, nums: List[int], k: int) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        
7        k = k % len(nums)
8        
9        i = 0
10        j = len(nums) - 1
11        while i < j: 
12            nums[i], nums[j] = nums[j], nums[i]
13            i += 1
14            j -= 1
15    
16        i = 0
17        j = k - 1
18        while i < j:
19            nums[i], nums[j] = nums[j], nums[i]
20            i += 1
21            j -=1
22        
23        i = k
24        j = len(nums) - 1
25        while i < j: 
26            nums[i], nums[j] = nums[j], nums[i]
27            i += 1
28            j -= 1
29        