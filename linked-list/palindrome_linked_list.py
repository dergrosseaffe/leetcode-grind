# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next: return True

        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverses right half
        previous = None
        while slow:
            temp      = slow.next
            slow.next = previous
            previous  = slow
            slow      = temp

        left, right = head, previous
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
