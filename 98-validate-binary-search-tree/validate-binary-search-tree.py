# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, root, mn, mx):
        if root is None:
            return True
        if root.val>mx or root.val<mn:
            return False
        left=self.check(root.left,mn,root.val-1)
        right=self.check(root.right,root.val+1,mx)
        return left and right

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check(root,-10000000000,10000000000)