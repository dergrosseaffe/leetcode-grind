# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        def max_gain(node: TreeNode) -> int:
            nonlocal max_sum

            if not node:
                return 0

            left = max(0, max_gain(node.left))
            right = max(0, max_gain(node.right))

            path_with_node = node.val + left + right
            max_sum = max(max_sum, path_with_node)

            return node.val + max(left, right)

        max_gain(root)
        return max_sum
