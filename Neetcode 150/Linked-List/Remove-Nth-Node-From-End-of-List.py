# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        index = 0
        while cur:
            index+=1
            cur = cur.next
        target = index-n-1
        if target < 0:
            return head.next
        
        cur = head
        i = 0
        while cur and i < target:
            cur = cur.next
            i+=1
        
        cur.next = cur.next.next if cur.next else None
        return head
        
