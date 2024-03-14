# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        # calculate length of list and gets tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # adjusts k
        k %= length
        if k == 0:
            return head

        # moves fast k positions onwards
        fast = head
        for _ in range(k):
            fast = fast.next

        # moves both pointers until fast reaches tail
        # after this, slow.next is the new head
        slow = head
        while fast.next:
            slow = slow.next
            fast = fast.next

        new_head = slow.next

        # rotates list
        slow.next = None    # Cuts the link between the end of the new tail and the new head
        tail.next = head

        return new_head
