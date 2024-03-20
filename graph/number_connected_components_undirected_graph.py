class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)

        visited = set()


        def visit(node: int) -> None:
            if node not in visited:
                visited.add(node)

                for neighbor in adj[node]:
                    visit(neighbor)


        # moves on edges
        components = 0
        for key in range(n):
            if key not in visited:
                visit(key)
                components += 1

        return components
