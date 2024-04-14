# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:


        def dfs(node: TreeNode, path_from_root: List[int]) -> None:
            nonlocal count

            if not node:
                return

            path_from_root.append(node.val)

            track = []
            path_sum = 0
            for value in reversed(path_from_root):
                path_sum += value
                track.append(value)
                if path_sum == targetSum:
                    count += 1

            dfs(node.left, path_from_root)
            dfs(node.right, path_from_root)

            path_from_root.pop()


        target_paths = []
        count = 0
        dfs(root, [])
        return count
