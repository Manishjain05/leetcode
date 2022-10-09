# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        :type root: TreeNode
        :rtype: bool
        """
        left_tree = root.left
        right_tree = root.right
        if root.left is None and root.right is None:
            return True
        return self.helper(root.left,root.right)
        
    def helper(self,p1,p2):
        
        if p1 is None and p2 is None:
            return True
        elif p1 is None or p2 is None:
            return False
        elif p1.val != p2.val:
            return False
        elif p1.val == p2.val:
            return self.helper(p1.left,p2.right) and self.helper(p1.right,p2.left)
        