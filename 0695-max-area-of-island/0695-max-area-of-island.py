
class Solution:
    def __init__(self):
        self.vis = [[0 for _ in range(101)] for _ in range(101)]
        self.max_area = 0
        self.current_area = 0

    def dfs(self, grid, i, j):
        rows = len(grid)
        cols = len(grid[0])
        self.max_area = max(self.max_area,self.current_area)
        if i+1<rows and self.vis[i+1][j] ==0 and grid[i+1][j]:
            self.vis[i+1][j] = 1
            self.current_area +=1
            self.dfs(grid, i + 1, j) 

        if i-1>=0 and self.vis[i-1][j] ==0 and grid[i-1][j]:
            self.vis[i-1][j] = 1
            self.current_area +=1
            self.dfs(grid, i - 1, j)  
        if j+1<cols and self.vis[i][j+1] ==0 and grid[i][j+1]:
            self.vis[i][j+1] = 1
            self.current_area +=1
            self.dfs(grid, i, j + 1)  
        if j-1>=0 and self.vis[i][j-1] ==0 and grid[i][j-1]:
            self.vis[i][j-1] = 1
            self.current_area +=1
            self.dfs(grid, i, j - 1) 

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        for i in range(101):
            for j in range(101):
                self.vis[i][j] = 0

        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0

        if rows == 0 or cols == 0:
            return 0

        nb = 0

        for i in range(rows):
            for j in range(cols):
                if self.vis[i][j] == 0 and grid[i][j] == 1:
                    self.vis[i][j] = 1
                    self.current_area = 1
                    self.dfs(grid, i, j)

        return self.max_area
