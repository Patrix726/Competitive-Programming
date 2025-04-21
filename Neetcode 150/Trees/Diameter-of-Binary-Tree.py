# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.diameter = 0
        def find_depth(root):
            if not root:
                return 0
            left = find_depth(root.left)
            right = find_depth(root.right)
            self.diameter = max(self.diameter,left+right)
            return max(left,right) + 1
        find_depth(root)
        return self.diameter
        
