# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        digit = 0
        num1 = 0
        num2 = 0
        while True:
            if not l1 and not l2:
                break
            if l1:
                num1 += l1.val * (10**digit) if digit > 0 else l1.val
                l1 = l1.next
            if l2:
                num2 += l2.val * (10**digit) if digit > 0 else l2.val
                l2 = l2.next

            digit += 1
        total = str(num1 + num2)
        HEAD = None
        TAIL = None
        for i in range(len(total) - 1, -1, -1):
            listNode = ListNode()
            listNode.val = int(total[i])
            listNode.next = None
            if i == len(total) - 1:
                HEAD = listNode
            else:
                TAIL.next = listNode
            TAIL = listNode
        return HEAD
