from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        ans = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0 or (row, col) in seen:
                    continue

                queue = deque([(row, col)])
                seen.add((row, col))
                area = 0

                while queue:
                    r, c = queue.popleft()
                    area += 1

                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nr = r + dr
                        nc = c + dc

                        if (0 <= nr < rows
                                and 0 <= nc < cols
                                and grid[nr][nc] == 1
                                and (nr, nc) not in seen):
                            seen.add((nr, nc))
                            queue.append((nr, nc))

                ans = max(ans, area)

        return ans