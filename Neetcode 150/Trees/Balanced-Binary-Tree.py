# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balanced = True
        def isbalanced(root):
            if not root:
                return 0
            left = isbalanced(root.left)
            right = isbalanced(root.right)

            if abs(right-left) > 1:
                self.is_balanced = False
            return max(left,right) + 1
        isbalanced(root)
        return self.is_balanced
        
