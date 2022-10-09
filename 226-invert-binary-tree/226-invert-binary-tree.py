# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        
        def swtch(n):
            # print("inside swicth func:")
            # print(n)
            if n is None:
                return 
            if n.left or n.right:
                # print("left: ", n.left)
                # print("right: ", n.right)
                tmp = n.right
                n.right = n.left
                n.left = tmp
#                 print("---------------")
#                 print("left: ", n.left)
#                 print("right: ", n.right)
        
        que = deque()
        que.append(root)
        while que:
            node = que.popleft()
            print(node)
            if node:
                que.append(node.left) 
                que.append(node.right)
                swtch(node)
        
        return root
            
            
        