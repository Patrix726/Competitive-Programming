# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findGoodNode(root: TreeNode, maximum: int) -> list[TreeNode]:
    maximum = max(maximum, root.val)
    arr = []
    if root.left:
        arr += findGoodNode(root.left, maximum)
    if root.right:
        arr += findGoodNode(root.right, maximum)

    if root.val == maximum:
        arr.append(root.val)

    return arr


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return len(findGoodNode(root, root.val))


obj = Solution()
fi = TreeNode(5)
f = TreeNode(1)
s = TreeNode(4, f, fi)
t = TreeNode(4)
fo = TreeNode(3, s, t)
print(obj.goodNodes(fo))
