
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        vis = [[0] * m for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if (grid[i][j]==2):
                    q.append((i,j))
        
        countMin = -1
        while len(q):
            x = len(q)
            for k in range(x):
                X = q.popleft()
                i,j = X[0],X[1]
                for l in range(-1,2):
                    for k in range(-1,2):
                        if abs(l-k)==1 and i+l in range(n) and j+k in range(m):
                            if grid[i+l][j+k]==1:
                                grid[i+l][j+k] = 2
                                q.append((i+l,j+k))
            countMin +=1
        test = True
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    test=False
        if test:
            return max(countMin,0)
        else:
            return -1
        
        
