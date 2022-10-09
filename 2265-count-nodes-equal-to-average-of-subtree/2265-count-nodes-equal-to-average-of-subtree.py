# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        que=deque()

        def fun(node):
            # print("inside fun: ", node.val)
            if node is None:
                return None
            q=deque()
            q.append(node)
            sm,n=0,0
            while q:
                n1=q.popleft()
                if n1:
                    sm += n1.val
                    n += 1
                    q.append(n1.left)
                    q.append(n1.right)
            print(sm,n,int(sm/n))
            return int(sm/n)
        
        que.append(root)
        cnt = 0
        while que:
            node = que.popleft()
            # print(node)
            if fun(node) is not None and fun(node)==node.val:
                
                cnt += 1
                # print(cnt)
            if node:
                que.append(node.left)
                que.append(node.right)
        return cnt
            
        
        