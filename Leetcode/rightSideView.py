# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        self.rightSide = []
        self.findRightSide(root, 1)

    def findRightSide(self, root: TreeNode, depth: int):
        if not root:
            return
        if depth > len(self.rightSide):
            self.rightSide.append(root.val)

        self.findRightSide(root.right, depth + 1)
        self.findRightSide(root.left, depth + 1)


obj = Solution()
fi = TreeNode(4, TreeNode(5), TreeNode(1))
f = TreeNode(13)
s = TreeNode(-3, TreeNode(-2))
t = TreeNode(-2, TreeNode(1, TreeNode(-1)), TreeNode(3))
fo = TreeNode(1, t, s)
print(obj.rightSideView(fo, -1))
