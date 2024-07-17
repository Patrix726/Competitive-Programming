# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        self.numOfPath = 0
        self.forAllRoots(root, 2)
        return self.numOfPath

    def forAllRoots(self, root: TreeNode, dir: int):
        if root is None:
            return
        if dir == 2:
            self.findZigZag(root.left, True, 0)
            self.findZigZag(root.right, False, 0)
        elif dir == 1:
            self.findZigZag(root.right, False, 0)
        else:
            self.findZigZag(root.left, True, 0)

        self.forAllRoots(root.left, 0)
        self.forAllRoots(root.right, 1)

    def findZigZag(self, root: TreeNode, left: bool, length: int):
        if root is None:
            return
        length += 1
        self.numOfPath = max(self.numOfPath, length)
        if left:
            self.findZigZag(root.right, False, length)
        else:
            self.findZigZag(root.left, True, length)


obj = Solution()
fi = TreeNode(4, TreeNode(5), TreeNode(1))
f = TreeNode(13)
s = TreeNode(-3, TreeNode(-2))
t = TreeNode(-2, TreeNode(1, TreeNode(-1)), TreeNode(3))
fo = TreeNode(1, t, s)
print(obj.pathSum(fo, -1))
