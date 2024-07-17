# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.numOfPath = 0
        self.forAllRoots(root, targetSum)
        return self.numOfPath

    def forAllRoots(self, root: TreeNode, targetSum: int):
        if root is None:
            return
        self.findPathSum(root, targetSum)
        self.forAllRoots(root.left, targetSum)
        self.forAllRoots(root.right, targetSum)

    def findPathSum(self, root: TreeNode, targetSum: int):
        if root is None:
            return
        if root.val == targetSum:
            self.numOfPath += 1

        self.findPathSum(root.left, targetSum - root.val)
        self.findPathSum(root.right, targetSum - root.val)


obj = Solution()
fi = TreeNode(4, TreeNode(5), TreeNode(1))
f = TreeNode(13)
s = TreeNode(-3, TreeNode(-2))
t = TreeNode(-2, TreeNode(1, TreeNode(-1)), TreeNode(3))
fo = TreeNode(1, t, s)
print(obj.pathSum(fo, -1))
