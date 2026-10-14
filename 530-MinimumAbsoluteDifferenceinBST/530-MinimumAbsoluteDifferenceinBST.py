# Last updated: 10/13/2026, 10:55:58 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
9        stack = []
10        curr = root
11        min_diff = float("inf")
12        prev = float("inf")
13
14        while curr or stack:
15            # reach bottom minimum value
16            while curr:
17                stack.append(curr)
18                curr = curr.left
19            
20            curr = stack.pop()
21            min_diff = min(min_diff, abs(prev - curr.val))
22            prev = curr.val
23            curr = curr.right
24
25        return min_diff
26    
27