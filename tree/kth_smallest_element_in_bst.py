# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        elements = []


        def inOrderTraversal(root: TreeNode) -> None:
            if not root: return

            inOrderTraversal(root.left)
            elements.append(root.val)
            inOrderTraversal(root.right)


        inOrderTraversal(root)
        return elements[k-1]
