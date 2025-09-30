class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n,m = len(board), len(board[0])
        visited = [[0] * m for _ in range(n)]

        def dfs(board, i, j):
            if i < 0 or i >= n or j < 0 or j >= m or board[i][j] == 'X' or visited[i][j]:
                return
            board[i][j] = 'E'
            visited[i][j] = 1
            dfs(board, i+1, j)
            dfs(board, i-1, j)
            dfs(board, i, j+1)
            dfs(board, i, j-1)

        for i in {0,n-1}:
            for j in range(m):
                if board[i][j] == 'O' and not visited[i][j]:
                    dfs(board, i, j)

        for j in {0,m-1}:
            for i in range(n):
                if board[i][j] == 'O' and not visited[i][j]:
                    dfs(board, i, j)
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'E':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        print(board)
        