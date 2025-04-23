# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ancestor = None
        def dfs(root,p,q):
            if not root:
                return False
            left = dfs(root.left,p,q)
            right = dfs(root.right,p,q)

            cur = root.val == p.val or root.val == q.val
            if (cur and left) or (cur and right) or (left and right):
                self.ancestor = root
                return False
            return cur or left or right
        dfs(root,p,q)
        return self.ancestor
            

            
