# Definition for a binary tree node.
from collections import defaultdict, deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverFromPreorder(self, traversal: str) -> TreeNode:
        root = TreeNode()
        nodeVals = []
        nodeDepths = []
        depth = 0
        values = traversal.split("-")
        for val in values:
            if not val:
                depth += 1
            else:
                nodeVals.append(int(val))
                nodeDepths.append(depth)
                depth = 1
        nodes = defaultdict(deque)
        root.val = int(nodeVals[0])
        nodes[0] = [root]
        for i in range(1, len(nodeVals)):
            value = nodeVals[i]
            dep = nodeDepths[i]

            parNode = nodes[dep - 1][-1]
            curNode = TreeNode()
            curNode.val = value
            if not parNode.left:
                parNode.left = curNode
            else:
                parNode.right = curNode
            nodes[dep].append(curNode)
        return root


ans = Solution()
print(ans.recoverFromPreorder("1-401--349---90--88"))
