# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def matches(root: TreeNode, subRoot: TreeNode) -> bool:
            if not root and not subRoot: return True
            if not root or not subRoot: return False
            if root.val != subRoot.val: return False

            return matches(root.left, subRoot.left) and matches(root.right, subRoot.right)


        def findRoot(root: TreeNode, subRoot: TreeNode) -> bool:
            if not root and not subRoot: return True
            if not root or not subRoot: return False

            if root.val == subRoot.val:
                if matches(root, subRoot):
                    return True

            return findRoot(root.left, subRoot) or findRoot(root.right, subRoot)


        return findRoot(root, subRoot)
