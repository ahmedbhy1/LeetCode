class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
       
       def dfs(i,j,tag):
           if vis[i][j]:
                return
           
           vis[i][j] = 1

           if tag == "pa":
                pa[i][j] = True
           else:
                at[i][j] = True
            
           
           if i+1<n and heights[i+1][j] >= heights[i][j]:
                dfs(i+1,j,tag)
           if i-1>=0 and heights[i-1][j] >= heights[i][j]:
                dfs(i-1,j,tag)
           if j-1>=0 and heights[i][j-1] >= heights[i][j]:
                dfs(i,j-1,tag)
           if j+1<m and heights[i][j+1] >= heights[i][j]:
                dfs(i,j+1,tag)

       n,m = len(heights),len(heights[0])
       vis = [[0]*m for _ in range(n)]
       pa = [[False]*m for _ in range(n)]
       at = [[False]*m for _ in range(n)]

       for j in range(m):
           dfs(0,j,"pa")
       
       for i in range(n):
           dfs(i,0,"pa")

       
       vis = [[0]*m for _ in range(n)]
       for j in range(m):
           dfs(n-1,j,"at")
       
       for i in range(n):
           dfs(i,m-1,"at")
    
       L = []
       for i in range(n):
           for j in range(m):
               if pa[i][j] and at[i][j]:
                   L.append([i,j])
       return L