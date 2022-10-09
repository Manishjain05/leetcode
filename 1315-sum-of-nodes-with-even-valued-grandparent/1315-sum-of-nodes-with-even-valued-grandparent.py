# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        self.sum = 0
        que=deque()
        
        def fun(node):
            # print("inside fun")
            if node and node.left:
                self.sum=self.sum+node.left.val
            if node and node.right:
                self.sum = self.sum+node.right.val
        
        
        que.append(root)
        while que:
            node = que.popleft()
            if node:
                que.append(node.left)
                que.append(node.right)
            if node and node.val%2==0 and node.left:
                fun(node.left)
            if node and node.val%2==0 and node.right:
                fun(node.right)
        
        return self.sum
        