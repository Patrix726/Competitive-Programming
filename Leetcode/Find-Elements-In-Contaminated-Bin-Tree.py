# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.tree = root

    def find(self, target: int) -> bool:
        path = []
        self.tree.val = 0
        while target > 0:
            if target % 2 == 0:
                target -= 2
                target //= 2
                path.append(1)
            else:
                target -= 1
                target //= 2
                path.append(0)
        cur = self.tree
        for dir in reversed(path):

            if dir == 1:
                if cur.right:
                    cur.right.val = cur.val * 2 + 2
                    cur = cur.right
                else:
                    return False
            else:
                if cur.left:
                    cur.left.val = cur.val * 2 + 1
                    cur = cur.left
                else:
                    return False
        return True
