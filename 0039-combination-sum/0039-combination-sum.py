class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        
        def dfs(subset,i=0):
            s = sum(subset)
            if i>=n or s>target:
                return 
            
            if s == target:
                res.append(subset.copy())
                return

            subset.append(candidates[i])
            dfs(subset.copy(),i)
            subset.pop()
            dfs(subset.copy(),i+1)
        
        dfs([],0)
        print(res)
        return res
            

            

