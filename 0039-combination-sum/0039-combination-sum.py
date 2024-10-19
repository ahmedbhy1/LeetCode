class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        n = len(candidates)
        
        def dfs(subset,i=0):
            print(subset,i)
            if i>=n:
                return 
            s = sum(subset)
            if s == target:
                res.add(tuple(subset))
            if s > target:
                return
            subset.append(candidates[i])
            dfs(subset.copy(),i)
            subset.pop()
            dfs(subset.copy(),i+1)
            
        dfs([],0)
        R = []
        for i in res:
            R.append(list(i))
        return R
            

            

