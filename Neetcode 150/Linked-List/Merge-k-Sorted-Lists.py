
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        head = None
        tail = None
        while True:
            all_none = True
            min_val = float('inf')
            min_idx = -1
            for idx,node in enumerate(lists):
                if not node:
                    continue
                all_none = False
                if node.val < min_val:
                    min_val = node.val
                    min_idx = idx
            if all_none:
                break
            if not head:
                head = lists[min_idx]
                lists[min_idx] = head.next
                head.next = None
                tail = head
            else:
                tail.next = lists[min_idx]
                lists[min_idx] = lists[min_idx].next
                tail = tail.next
                tail.next = None
        return head


