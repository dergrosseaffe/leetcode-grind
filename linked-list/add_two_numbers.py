# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        carry = 0
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            sum = (a + b + carry) % 10
            carry = 1 if (a + b + carry) // 10 > 0 else 0

            tail.next = ListNode(sum)

            if l1: l1 = l1.next
            if l2: l2 = l2.next
            tail = tail.next

        if carry:
            tail.next = ListNode(1)

        return dummy.next
