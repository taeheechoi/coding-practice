# https://leetcode.com/problems/number-of-islands/discuss/1814139/SIMPLE-Python-DFS-Solution-O(N-*-M)

# https://www.youtube.com/watch?v=__98uL6wst8


def dfs(self, grid, x, y, r, c):
    if x < 0 or x >= r or y < 0 or y >= c or grid[x][y] != '1':
        return
    grid[row][col] = '2'
    self.dfs(grid, x+1, y, r, c)
    self.dfs(grid, x-1, y, r, c)
    self.dfs(grid, x, y+1, r, c)
    self.dfs(grid, x, y-1, r, c)



def numIslands(self, grid):
    islands = 0
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                self.dfs(grid, i, j, rows, cols)
                islands += 1

    return islands