class Solution:
    def change(self, amount: int,coins: list[int]) -> int:
        if amount == 0:
            return 1
        m = (amount)
        n = len(coins)
        dp=[[0 for i in range(m)]for j in range(n)]
        for i in range(n):
            for j in range(m):
                if coins[i]-1 == j:
                    dp[i][j] = 1

        for i in range(n):
            for j in range(m):
                if i-1>=0:
                    dp[i][j] += dp[i-1][j]
                if j-coins[i]>=0:
                    dp[i][j] += dp[i][j-coins[i]]                
        return dp[-1][-1]