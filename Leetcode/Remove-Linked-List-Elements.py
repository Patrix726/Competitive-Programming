
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        current = head
        previous = None
        while current:
            if current.val == val:
                if previous == None:
                    head = current.next
                else:
                    previous.next = current.next
            else:
                previous = current
            current = current.next
        return head
            
