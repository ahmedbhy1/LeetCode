class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ws = set(wordDict)
        ch = s
        @cache
        def dfs(ch):
            n = len(ch)
            if n == 0:
                return True
            x = ""
            test = False
            for i in range(n):
                x+=ch[i]
                if x in ws:
                    if i+1 <= n:
                        test = test or dfs(ch[i+1:])

            return test
        return dfs(ch)