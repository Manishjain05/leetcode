# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.left is None and root.right is None:
            return root.val
        
        lvl_nodes = [[]]
        self.mx=0
        visit = set()
        lvl = 1
        lvl_nodes.append([root.val])
        que=deque()
        que.append((root,lvl))
        
        def lvl_node(n,h):
            if n is None:
                return
            if n.left:
                self.mx = max(self.mx,h+1)
                # print(ht+1)
                # print(lvl_nodes)
                lvl_nodes[ht+1].append(n.left.val)
            if n.right:
                self.mx = max(self.mx,h+1)
                lvl_nodes[ht+1].append(n.right.val)
            
        
        while que:
            node,ht = que.popleft()
            if ht not in visit:
                visit.add(ht)
                lvl_nodes.append([])
            if node.left:
                que.append((node.left,ht+1))
            if node.right:
                que.append((node.right,ht+1))
            lvl_node(node,ht)
            

        return sum(lvl_nodes[self.mx])
        