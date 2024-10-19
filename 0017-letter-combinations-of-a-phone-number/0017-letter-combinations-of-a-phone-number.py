class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n ==0:
            return []
        d = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z'],
        }
        L=[]
        def dfs(i,ch):
            if i>=n:
                L.append(ch)
                return
            for q in d[digits[i]]:
                dfs(i+1,ch+q)
        dfs(0,"")
        return L
            
        