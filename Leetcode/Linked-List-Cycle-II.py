
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        has_cycle = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                has_cycle = True
                break
        if not has_cycle:
            return None
        slow2 = head
        while slow2 != slow:
            slow2 = slow2.next
            slow = slow.next
        return slow
