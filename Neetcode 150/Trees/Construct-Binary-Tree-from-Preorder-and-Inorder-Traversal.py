from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        n = len(preorder)
        self.order_hash = defaultdict(list)
        for idx,val in enumerate(preorder):
            self.order_hash[val].append(idx)
        for idx,val in enumerate(inorder):
            self.order_hash[val].append(idx)
        self.visited = []
        def fill_nodes(value, upper_limit, lower_limit):
            root = TreeNode(val=value)
            self.visited.append(value)
            inorder_idx = self.order_hash[value][1]
            left = self.order_hash[self.visited[-1]][0] + 1
            if inorder_idx != lower_limit + 1 and left < len(preorder):
                root.left = fill_nodes(preorder[left],inorder_idx, lower_limit)
            else:
                right = left
            right = self.order_hash[self.visited[-1]][0] + 1
            if inorder_idx != upper_limit - 1 and right < len(preorder):
                root.right = fill_nodes(preorder[right], upper_limit, inorder_idx)
            return root
        return fill_nodes(preorder[0],n,-1)
