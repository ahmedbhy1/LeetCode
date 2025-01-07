class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        INF = 999999999 
        dp=[INF]*(amount+1)
        dp[0] = 0
        for i in coins:
            if i<= amount:
                dp[i] = 1
        for i in range(1,amount+1):
            for j in range(len(coins)):
                if i-coins[j]>0 and dp[i-coins[j]]>0:
                    dp[i] = min(dp[i],1+dp[i-coins[j]])
        if dp[amount] == INF:
            return -1
        return dp[amount]