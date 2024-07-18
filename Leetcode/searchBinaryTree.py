from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        queue = deque()
        queue.append(root)

        while queue:
            lq = len(queue)

            for i in range(lq):
                node = queue.popLeft()
                if node.val == val:
                    return node
                if node:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
        return None


obj = Solution()
fi = TreeNode(4, TreeNode(5), TreeNode(1))
f = TreeNode(13)
s = TreeNode(-3, TreeNode(-2))
t = TreeNode(-2, TreeNode(1, TreeNode(-1)), TreeNode(3))
fo = TreeNode(1, t, s)
print(obj.searchBST(fo, -1))
