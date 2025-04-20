
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        total = 0
        while cur:
            cur = cur.next
            total+=1
        rem = total % k
        dummyhead = ListNode()
        tail = dummyhead
        cur = head
        count = 0
        while True:
            if total - count == rem:
                tail.next = cur
                break
            temp_tail = None
            idx = 0
            while cur and idx < k:
                if not temp_tail:
                    temp_tail = cur
                temp = cur
                cur = cur.next
                temp.next = tail.next
                tail.next = temp
                idx+=1
            count+=idx
            tail = temp_tail
        return dummyhead.next
