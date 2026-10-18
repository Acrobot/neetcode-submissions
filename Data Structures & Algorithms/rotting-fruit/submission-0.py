ROTTEN = 2
FRESH = 1
EMPTY = 0

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        is_fruit = set()
        visited = set()
        q = deque()

        # Find rotten fruit
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                val = grid[y][x]
                if val == EMPTY:
                    continue

                is_fruit.add((x, y))

                if val == ROTTEN:
                    q.append((x, y, 0))  # fruit at (x, y) is rotten from tick 0

        max_tick = 0

        while q:
            x, y, tick = q.popleft()

            if not (x, y) in is_fruit or (x, y) in visited:
                continue

            visited.add((x, y))

            q.append((x+1, y, tick+1))
            q.append((x-1, y, tick+1))
            q.append((x, y+1, tick+1))
            q.append((x, y-1, tick+1))

            max_tick = max(max_tick, tick)

        return max_tick if len(visited) == len(is_fruit) else -1

