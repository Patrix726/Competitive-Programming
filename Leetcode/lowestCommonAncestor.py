# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        self.ancestors = []
        self.findAncestors(root, [], [p, q])
        lca = root
        for i in range(min(len(self.ancestors[0]), len(self.ancestors[1]))):
            if self.ancestors[0][i] != self.ancestors[1][i]:
                lca = self.ancestors[0][i - 1]
                break
        return lca

    def findAncestors(
        self, root: TreeNode, ancestors: list[TreeNode], targetNodes: list[TreeNode]
    ):
        if root is None:
            return
        if root == targetNodes[0]:
            self.ancestors.append(ancestors + [root])
        if root == targetNodes[1]:
            self.ancestors.append(ancestors + [root])
        else:
            self.findAncestors(root.left, ancestors + [root], targetNodes)
            self.findAncestors(root.right, ancestors + [root], targetNodes)


obj = Solution()
fi = TreeNode(4, TreeNode(5), TreeNode(1))
f = TreeNode(13)
s = TreeNode(-3, f)
t = TreeNode(-2, TreeNode(1, TreeNode(-1)), fi)
fo = TreeNode(1, t, s)
print(obj.lowestCommonAncestor(fo, f, fi))
