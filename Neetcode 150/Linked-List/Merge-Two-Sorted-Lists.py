# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2
        if not cur1:
            return cur2
        if not cur2:
            return cur1
        head = ListNode(cur1.val,None) if cur1.val < cur2.val else ListNode(cur2.val,None)
        tail = head
        if cur1.val < cur2.val:
            cur1 = cur1.next
        else:
            cur2 = cur2.next
        while cur1 and cur2:
            if cur1.val < cur2.val:
                tail.next = ListNode(cur1.val,None)
                cur1 = cur1.next
            else:
                tail.next = ListNode(cur2.val,None)
                cur2 = cur2.next
            tail = tail.next
        if cur1:
            tail.next = cur1
        if cur2:
            tail.next = cur2
        return head

        


        
