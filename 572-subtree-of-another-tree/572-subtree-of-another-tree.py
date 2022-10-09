# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        que=deque()
        
        def dfs(node1,node2):
            print("inside dfs")
            quetmp = deque()
            quetmp.append((node1,node2))
            while quetmp:
                
                
                n1,n2 = quetmp.popleft()
                
                if n1 is None and n2 is None:
                    pass
                elif (n1 is None and n2 is not None) or (n1 is not None and n2 is None) or (n1.val!=n2.val):
                    return False
                if n1 and n2:
                    
                    quetmp.append((n1.left,n2.left))
                    
                    quetmp.append((n1.right,n2.right))
                    
            
            return True
        
        que.append(root)
        while que:
            node=que.popleft()
            
            if node.val==subRoot.val:
                flag=dfs(node,subRoot)
                if flag==True:
                    return True
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        
        return False
        