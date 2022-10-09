# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        que = deque()
        que.append(root)
        val = root.val
        
        def ret_val(n):
            if n:
                return True if n.val==val else False
            else:
                return True
        
        while que:
            node = que.popleft()
            if not ret_val(node) and node:
                return False
            if ret_val(node) and node:
                que.append(node.left)
                que.append(node.right)
            
        return True
        
        