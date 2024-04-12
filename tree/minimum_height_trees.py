class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        nodes = {node: [] for node in range(n)}

        for n1, n2 in edges:
            nodes[n1].append(n2)
            nodes[n2].append(n1)

        leaves = [leaf for leaf in nodes.keys() if len(nodes[leaf]) == 1]
        while len(nodes) > 2:
            for leaf in leaves:
                if nodes[leaf]:
                    neighbor = nodes[leaf].pop()
                    nodes[neighbor].remove(leaf)

                del nodes[leaf]

            leaves = [leaf for leaf in nodes.keys() if len(nodes[leaf]) <= 1]

        return leaves
