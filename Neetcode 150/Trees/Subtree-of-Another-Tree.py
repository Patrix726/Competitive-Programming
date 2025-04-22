# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.is_subtree = False
        def issubtree(root1, root2):
            if not root1 and not root2:
                return True
            elif not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False
            return issubtree(root1.left,root2.left) and issubtree(root1.right,root2.right)
        def dfs(root,target):
            if not root:
                return
            
            if root.val == target.val:
                self.is_subtree = self.is_subtree or issubtree(root,target)
            dfs(root.left,target)
            dfs(root.right, target)
        dfs(root, subRoot)
        return self.is_subtree
