# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None, low=float("-inf"), high=float("inf")) -> bool:
        if not low < root.val < high:
            return False

        if root.right:
            if not self.isValidBST(root.right, root.val, high):
                return False

        if root.left:
            if not self.isValidBST(root.left, low, root.val):
                return False
        
        return True
