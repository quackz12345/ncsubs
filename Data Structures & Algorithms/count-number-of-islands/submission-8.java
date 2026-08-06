

class Solution {
    public int numIslands(char[][] grid) {
        Deque<int[]> stack = new ArrayDeque<int[]>();
        int count = 0;
        int g = grid.length;
        for (int i = 0; i < g; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j] == '1') {
                    stack.push(new int[]{i, j});
                    count++;
                }
                int cx = 0, cy = 0;
                while (!stack.isEmpty()) {
                    int[] p = stack.pop();
                    cx = p[0];
                    cy = p[1];
                    if (grid[cx][cy] == '1') {
                        grid[cx][cy] = '0';
                        if (cx - 1 >= 0) stack.push(new int[]{cx - 1, cy});
                        if (cx + 1 < g) {stack.push(new int[]{cx + 1, cy}); j++;}
                        if (cy - 1 >= 0) stack.push(new int[]{cx, cy - 1});
                        if (cy + 1 < grid[i].length) stack.push(new int[]{cx, cy + 1});
                    }
                }
            }
        }
        return count;
    }
}