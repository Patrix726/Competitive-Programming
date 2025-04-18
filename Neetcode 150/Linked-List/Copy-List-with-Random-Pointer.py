"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        org_node = head
        new_node = None
        if not head:
            return new_node
        while org_node:
            new_node = Node(x=org_node.val,next=org_node.next)
            org_node.next = new_node
            org_node = org_node.next.next
        
        new_node_head = head.next
        org_node = head
        cur_node = new_node_head
        while cur_node:
            cur_node.random = org_node.random.next if org_node.random else None
            org_node = org_node.next.next
            cur_node = cur_node.next.next if cur_node.next else None
        cur = new_node_head
        while cur.next:
            cur.next = cur.next.next
            cur = cur.next
        return new_node_head
        
