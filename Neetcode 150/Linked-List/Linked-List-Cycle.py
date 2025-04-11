# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        while cur and cur.next != None:
            try:
                if cur.visited:
                    return True
            except:
                pass
            cur.visited = True
            cur = cur.next
        return False
