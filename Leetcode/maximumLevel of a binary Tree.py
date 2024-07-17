from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        queue = deque()
        queue.append(root)
        maxSum = root.val
        maxLevel = level = 1
        while queue:
            lq = len(queue)
            curSum = 0
            valid = False
            for i in range(lq):
                node = queue.popleft()
                if node:
                    valid = True
                    curSum += node.val
                    queue.append(node.left)
                    queue.append(node.right)
            if valid and curSum > maxSum:
                maxLevel = level
                maxSum = curSum
            level += 1
        return maxLevel
