class Solution:
    def numDecodings(self, s: str) -> int:
        if(s[0]=='0'): return 0
        if len(s) == 1: return 1
        if (int(s[0]) > 2 and int(s[1]) == 0):
            return 0
        n = len(s)
        dp = [0] * (n)
        dp [0] = 1
        if (int(s[0]+s[1]) < 27 and int(s[1]) != 0):dp [1] = 2 
        else:dp[1] = 1
        for i in range(2,n):
            if (int(s[i-1]+s[i]) < 27 and int(s[i])>0 and int(s[i-1])>0):dp [i] = dp[i-2] + dp[i-1]
            else: 
                if int(s[i]) == 0:
                    if int(s[i-1])==0 or int(s[i-1])>2:
                        return 0
                    dp[i] = dp[i-2]
                else:
                    dp[i] = dp[i-1]
        return dp[-1]