
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def invert(root):
            if not root:
                return None
            left_invert = invert(root.right)
            right_invert = invert(root.left)
            root.left = left_invert
            root.right = right_invert
            return root
        return invert(root)
