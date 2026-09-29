# Last updated: 9/29/2026, 12:05:36 PM
1class Solution:
2    def rob(self, nums: list[int]) -> int:
3        """
4        at each index two options => rob, don't rob
5        condition to rob, adjacent house has not been robbed and the list is a loop
6
7        nums = [2, 3, 2]
8        
9        break into two dp problems and find the max:
10            go from 0:n -1 and from 1:n
11
12        index 0 and -1 are considered adjacent
13
14        """
15        if len(nums) == 1:
16            return nums[0]
17
18        elif len(nums) == 2:
19            return max(nums)
20
21        dp1 = [0] * (len(nums) - 1)
22        dp2 = [0] * (len(nums) - 1)
23        
24        for i in range(len(nums) - 1):
25            dp1[i] = max(nums[i] + dp1[i - 2], dp1[i - 1])
26        
27        for i in range(1, len(nums)):
28            dp2[i - 1] = max(nums[i] + dp2[i - 3], dp2[i - 2])
29
30        return max(dp1[-1], dp2[-1])
31        