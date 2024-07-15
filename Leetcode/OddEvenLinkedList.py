# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        odd = oddEnd = head
        even = evenEnd = head.next

        while evenEnd and evenEnd.next:
            oddEnd.next = evenEnd.next
            oddEnd = oddEnd.next
            if oddEnd:
                evenEnd.next = oddEnd.next
                evenEnd = evenEnd.next
        oddEnd.next = even

        return odd


obj = Solution()
f = ListNode(4)
s = ListNode(3, f)
t = ListNode(2, s)
fo = ListNode(1, t)
obj.oddEvenList(fo)
