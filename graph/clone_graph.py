"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
   def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None

        nodes = {}
        def dfs(node):
            # new node already created
            if node in nodes:
                return nodes[node]

            # creates new node
            newNode = Node(node.val)
            nodes[node] = newNode

            for neighbor in node.neighbors:
                newNode.neighbors.append(dfs(neighbor))

            return newNode

        return dfs(node)
