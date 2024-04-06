# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return '[]'

        queue = deque([root])

        r = []
        while queue:
            node = queue.popleft()

            if node:
                r.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                r.append(None)

        # removes trailing None values
        while r[-1] == None:
            r.pop()

        return str(r)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        if data == '[]':
            return []

        values = eval(data)
        root = TreeNode(values[0])
        queue = deque([root])

        i = 1
        while queue:
            node = queue.popleft()

            if i < len(values) and values[i] != None:
                left = TreeNode(values[i])
                node.left = left
                queue.append(left)
            i += 1

            if i < len(values) and values[i] != None:
                right = TreeNode(values[i])
                node.right = right
                queue.append(right)
            i += 1

        return root





# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))