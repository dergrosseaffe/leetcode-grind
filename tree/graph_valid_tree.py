class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {node: [] for node in range(n)}

        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        def dfs(node: int, parent: int):
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited or not dfs(neighbor, node):
                    return False

            return True

        visited = set()
        return dfs(0, None) and len(visited) == n
