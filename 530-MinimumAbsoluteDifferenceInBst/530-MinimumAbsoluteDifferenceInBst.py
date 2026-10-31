# Last updated: 10/31/2026, 6:29:04 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack = []
        curr = root
        min_diff = float("inf")
        prev = None

        while curr or stack:
            # reach bottom minimum value
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            
            if prev is not None:
                min_diff = min(min_diff, curr.val - prev)
            
            prev = curr.val
            curr = curr.right

        return min_diff
    
