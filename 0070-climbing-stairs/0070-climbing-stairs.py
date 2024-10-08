class Solution:
    DP=[0]*46
    def climbStairs(self, n: int) -> int:
        if not self.DP[1]:
            self.DP[1] = 1 
            self.DP[2] = 2
            for i in range(3,46):
                self.DP[i]=self.DP[i-1]+self.DP[i-2]
        
        return self.DP[n]