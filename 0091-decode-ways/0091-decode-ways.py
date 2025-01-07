
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        n = len(s)
        if n == 1: return 1
        dp = [1, 1 if s[1] != '0' else 0]
        if 10 <= int(s[:2]) <= 26: dp[1] += 1
        
        for i in range(2, n):
            if s[i] == '0':
                if s[i-1] in '12': dp.append(dp[-2])
                else: return 0
            elif 10 <= int(s[i-1:i+1]) <= 26:
                dp.append(dp[-1] + dp[-2])
            else:
                dp.append(dp[-1])
        
        return dp[-1]
