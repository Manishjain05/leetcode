# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        que = deque()
        visit = set()
        
        que.append(root)
        while que:
            node = que.popleft()
            if node and (k-node.val) in visit:
                return True
            elif node:
                visit.add(node.val)
                que.append(node.left)
                que.append(node.right)
        
        return False
        