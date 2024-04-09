# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        new_head = head.next
        prev = None
        while head and head.next:
            a, b = head, head.next
            a.next, b.next = b.next, a

            if prev:
                prev.next = b

            prev = head
            head = head.next

        return new_head
