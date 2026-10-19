class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False

        connections = [set() for _ in range(n)]

        for edge in edges:
            connections[edge[0]].add(edge[1])
            connections[edge[1]].add(edge[0])

        q: list[tuple[int, int | None]] = [(0, None)]  # Start from idx 0, because we can start anywhere
        visited = set()

        while q:
            elem, parent = q.pop()

            if elem in visited:
                return False

            visited.add(elem)

            for c in connections[elem]:
                if c == parent:
                    continue  # we'd be backtracking

                q.append((c, elem))

        return len(visited) == n
