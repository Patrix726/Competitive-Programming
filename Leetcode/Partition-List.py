# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        left = None
        right = None
        right_head = None
        dummy.next = left
        cur = head
        while cur:
            if cur.val < x:
                if left:
                    left.next = cur
                else:
                    dummy.next = cur
                left = cur
            else:
                if right:
                    right.next = cur
                else:
                    right_head = cur
                right = cur
            cur = cur.next
        if not left:
            dummy.next = right_head
        else:
            left.next = right_head
        if right:
            right.next = None
        return dummy.next
