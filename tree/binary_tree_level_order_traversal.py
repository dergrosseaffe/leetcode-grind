# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None: return []

        queue = [root]
        order = []

        while (queue):
            level = []
            for i in range(len(queue)):
                element = queue.pop(0)
                level.append(element.val)

                if element.left:  queue.append(element.left)
                if element.right: queue.append(element.right)

            order.append(level)

        return order
