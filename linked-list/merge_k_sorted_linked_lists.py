# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        for l in lists:
            while l != None:
                heappush(h, l.val)
                l = l.next

        head = ListNode(0)
        current = head
        while h:
            current.next = ListNode(heappop(h))
            current = current.next

        return head.next
