class Solution {
    Set<Integer> seen = new HashSet<>();

    public int maxAreaOfIsland(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;

        List<Integer>[] graph = new ArrayList[rows * cols];

        for (int i = 0; i < rows * cols; i++)
            graph[i] = new ArrayList<>();

        // Convert grid into graph
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {

                if (grid[r][c] == 0)
                    continue;

                int node = r * cols + c;

                // up
                if (r > 0 && grid[r - 1][c] == 1)
                    graph[node].add((r - 1) * cols + c);

                // down
                if (r < rows - 1 && grid[r + 1][c] == 1)
                    graph[node].add((r + 1) * cols + c);

                // left
                if (c > 0 && grid[r][c - 1] == 1)
                    graph[node].add(r * cols + c - 1);

                // right
                if (c < cols - 1 && grid[r][c + 1] == 1)
                    graph[node].add(r * cols + c + 1);
            }
        }

        int max = 0;

        // Find connected components
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {

                if (grid[r][c] == 1) {
                    int node = r * cols + c;

                    if (!seen.contains(node)) {
                        seen.add(node);
                        max = Math.max(max, dfs(node, graph));
                    }
                }
            }
        }

        return max;
    }

    public int dfs(int node, List<Integer>[] graph) {
        int area = 1;

        for (int neighbor : graph[node]) {
            if (!seen.contains(neighbor)) {
                seen.add(neighbor);
                area += dfs(neighbor, graph);
            }
        }

        return area;
    }
}