# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next: return True

        middle = head
        steps = 0
        stack = []
        stack.append(head.val)
        while head:
            steps += 1
            if steps % 2 == 0:
                middle = middle.next
                stack.append(middle.val)

            head = head.next

        if (steps % 2 == 0):
             stack.pop()

        while middle:
            if middle.val == stack.pop():
                middle = middle.next
            else:
                return False

        return not stack
