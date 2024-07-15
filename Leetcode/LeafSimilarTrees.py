# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findLeaf(root: TreeNode) -> list[TreeNode]:
    if root.left == None and root.right == None:
        return [root.val]
    else:
        left = findLeaf(root.left) if root.left else None
        right = findLeaf(root.right) if root.right else None

        if left and right:
            return left + right
        else:
            return left if left else right


class Solution:
    def leafSimilar(self, root: TreeNode) -> int:
        return findLeaf(root)


obj = Solution()
fi = TreeNode(5)
f = TreeNode(4)
s = TreeNode(3, f, fi)
t = TreeNode(2)
fo = TreeNode(1, s, t)
print(obj.leafSimilar(fo))
