# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur and cur.next:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        cur.next = prev
        return cur


obj = Solution()
f = ListNode(4)
s = ListNode(3, f)
t = ListNode(2, s)
fo = ListNode(1, t)
obj.reverseList(fo)
