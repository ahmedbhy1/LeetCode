class Solution:
    def climbStairs(self, n: int) -> int:
        DP=[0]*46
        DP[1] = 1 
        DP[2] = 2
        for i in range(3,46):
            DP[i]=DP[i-1]+DP[i-2]
        return DP[n]