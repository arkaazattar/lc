# Last updated: 5/23/2026, 2:33:43 PM
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        last_1 = m - 1
        last_2 = n - 1 
        last = m + n - 1

        while last_2 >= 0:
            if last_1 >= 0 and nums1[last_1] > nums2[last_2]:
                nums1[last] = nums1[last_1]
                last_1 -= 1
            else:
                nums1[last] = nums2[last_2]
                last_2 -= 1
            last -= 1
            
                