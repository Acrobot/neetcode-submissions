class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        visited = set()
        
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if (x, y) in visited:
                    continue

                area = 0
                q = [(x, y)]

                while q:
                    e_x, e_y = q.pop()
                    if (not 0 <= e_y < len(grid)) \
                    or (not 0 <= e_x < len(grid[0])) \
                    or (e_x, e_y) in visited \
                    or grid[e_y][e_x] == 0:
                        continue

                    area += 1
                    visited.add((e_x, e_y))

                    q.append((e_x+1, e_y))
                    q.append((e_x-1, e_y))
                    q.append((e_x, e_y+1))
                    q.append((e_x, e_y-1))

                max_area = max(max_area, area)

        return max_area

