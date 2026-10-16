class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()

        def dfs(x: int, y: int) -> None:
            if y < 0 or not y < len(grid) or x < 0 or not x < len(grid[0]) or (x, y) in visited:
                return

            visited.add((x, y))

            if grid[y][x] == '0':
                return
            else:
                dfs(x - 1, y)
                dfs(x + 1, y)
                dfs(x, y - 1)
                dfs(x, y + 1)

        islands = 0

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if (x, y) in visited or grid[y][x] == '0':
                    continue

                # print(f"island start: {x}, {y}, visited: {visited}")
                dfs(x, y)
                islands += 1

        return islands
