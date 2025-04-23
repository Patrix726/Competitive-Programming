
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.is_valid = True
        def dfs(root):
            if not root:
                return
            
            cur = root.val
            left = dfs(root.left)
            right = dfs(root.right)
            if (left and left[1] >= cur) or (right and right[0]<=cur):
                self.is_valid = False
            min_val = left[0] if left else cur
            max_val = right[1] if right else cur
            return (min_val,max_val)
        dfs(root)
        return self.is_valid
            
