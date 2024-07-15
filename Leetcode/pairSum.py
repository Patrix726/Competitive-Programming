# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: ListNode) -> ListNode:
        arr = []
        maxSum = 0
        while head:
            arr.append(head)
            head = head.next
        for i in range(len(arr) / 2):
            if i != len(arr) - 1 - i:
                s = arr[i] + arr[-i - 1]
            if s > maxSum:
                maxSum = s
        return maxSum


obj = Solution()
f = ListNode(4)
s = ListNode(3, f)
t = ListNode(2, s)
fo = ListNode(1, t)
obj.reverseList(fo)
