class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connections = [set() for _ in range(n)]
        visited = [False for _ in range(n)]

        for edge in edges:
            connections[edge[0]].add(edge[1])
            connections[edge[1]].add(edge[0])

        groups = 0

        for idx in range(n):
            if visited[idx]:
                continue

            # print(visited)

            groups += 1

            q = [idx]
            while q:
                node = q.pop()
                if visited[node]:
                    continue
                visited[node] = True
                q.extend(connections[node])

        return groups


                
