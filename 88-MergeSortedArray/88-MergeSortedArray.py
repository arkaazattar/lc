# Last updated: 10/21/2026, 11:01:52 PM
1class Solution:
2    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
3        """
4        Do not return anything, modify nums1 in-place instead.
5        
6        """
7        m = m - 1
8        n = n - 1
9        for i in range(len(nums1) - 1, -1, -1):
10            if m < 0:
11                nums1[i] = nums2[n]
12                n -= 1
13
14            elif n < 0:
15                break
16                
17            elif nums2[n] > nums1[m]:
18                nums1[i] = nums2[n]
19                n = n - 1
20            else:
21                nums1[i] = nums1[m]
22                m = m - 1
23