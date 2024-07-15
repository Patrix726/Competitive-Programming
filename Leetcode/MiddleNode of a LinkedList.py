# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        arr = []
        while head:
            arr.append(head)
            head = head.next

        middle = int(len(arr) / 2)
        if middle == 0:
            return None
        elif middle == len(arr) - 1:
            arr[0].next = None
            return arr[0]
        else:
            arr[middle - 1].next = arr[middle + 1]
            return arr[0]


obj = Solution()
f = ListNode(4)
s = ListNode(3, f)
t = ListNode(2, s)
fo = ListNode(1, t)
obj.deleteMiddle(fo)
