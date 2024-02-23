# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue1 = []
        queue2 = []
        queue1.append(root)
        queue = queue1
        other_queue = queue2

        order = []
        while (queue):
            level = []
            while (queue):
                element = queue.pop(0)
                if not element: continue

                # adds level children to the other queue
                other_queue.append(element.left)
                other_queue.append(element.right)
                level.append(element.val)

            if (level):
                order.append(level.copy())
            level.clear()
            queue.clear()
            # swap queues
            queue, other_queue = other_queue, queue

        return order
