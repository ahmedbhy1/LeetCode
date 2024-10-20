class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxx = 0
        L=[0]
        n,m = len(grid),len(grid[0])
        vis = [[0] * m for _ in range(n)]
        
        def dfs(i,j):
            if i<0 or i>n or j>m or j<0:
                return 
            for l in range(-1,2):
                for k in range(-1,2):
                    test = i+l>=0 and i+l<n and j+k>=0 and j+k<m
                    if (test and grid[i+l][j+k]==1 and vis[i+l][j+k]==0) and abs(l-k)==1:
                        vis[i+l][j+k] = 1
                        L[-1]+=1
                        dfs(i+l,j+k)



        for i in range(n):
            for j in range(m):
                if (grid[i][j]==1 and vis[i][j]==0):
                    vis[i][j] = 1
                    L.append(1)
                    dfs(i,j)
        
        return max(L)