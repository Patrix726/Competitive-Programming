# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maximum = float('-inf')
        def dfs(root):
            if not root:
                return None
            cur = root.val
            left = dfs(root.left)
            right = dfs(root.right)
            maximum = cur
            maximum = max(maximum,cur+left) if left else maximum
            maximum = max(maximum,cur+right) if right else maximum
            join_maximum = cur+left+right if left and right else float('-inf')
            self.maximum = max(maximum, self.maximum,join_maximum)
            return maximum
        dfs(root)
        return self.maximum
