# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        def merge(left: ListNode, right: ListNode) -> ListNode:
            dummy = ListNode(0)
            tail = dummy

            while left and right:
                if left.val < right.val:
                    tail.next = left
                    left = left.next
                else:
                    tail.next = right
                    right = right.next
                tail = tail.next

            tail.next = left or right

            return dummy.next


        def mergesort(head: ListNode) -> ListNode:
            # move slow to middle of list to divide it
            if not head or not head.next:
                return head

            prev, fast, slow = None, head, head
            while fast and fast.next:
                prev, slow, fast = slow, slow.next, fast.next.next

            if prev:
                prev.next = None

            left = mergesort(head)
            right = mergesort(slow)

            return merge(left, right)


        return mergesort(head)
