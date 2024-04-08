# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        nodes = defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            node, depth = queue.popleft()
            nodes[depth].append(node.val)

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        r = []
        for depth, node_list in nodes.items():
            if depth % 2 == 0:
                r.append(node_list[:])
            else:
                r.append(node_list[::-1])

        return r
