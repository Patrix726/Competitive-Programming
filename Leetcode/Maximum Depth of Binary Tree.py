# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findDepth(root: TreeNode, depth: int) -> int:
    if root.left == None and root.right == None:
        return depth + 1
    else:
        depth += 1
        output = depth
        if root.left:
            left = findDepth(root.left, depth)
            output = max(output, left)
        if root.right:
            right = findDepth(root.right, depth)
            output = max(output, right)
        return output


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return findDepth(root, 0)


obj = Solution()
fi = TreeNode(4)
f = TreeNode(4)
s = TreeNode(3, f, fi)
t = TreeNode(2)
fo = TreeNode(1, s, t)
print(obj.maxDepth(fo))
