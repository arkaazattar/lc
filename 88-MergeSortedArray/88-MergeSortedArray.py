# Last updated: 10/8/2026, 1:51:34 PM
1class Solution:
2    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
3        """
4        Do not return anything, modify nums1 in-place instead.
5
6        """
7        r1, r2 = m - 1, n - 1
8        for i in range(len(nums1) - 1, -1, -1):
9            # i is the insertion
10            if r1 < 0:
11                nums1[i] = nums2[r2]
12                r2 -= 1
13            elif r2 < 0:
14                nums1[i] = nums1[r1]
15                r1 -= 1
16            
17            elif nums1[r1] > nums2[r2]:
18                nums1[i] = nums1[r1]
19                r1 -= 1
20
21            elif nums1[r1] <= nums2[r2]:
22                nums1[i] = nums2[r2]
23                r2 -= 1
24
25            
26        