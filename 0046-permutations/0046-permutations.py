class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def dfs(l,s):
            
            if len(l)>=n:
                res.append(l.copy())
                return 

            for j in range(n):
                if nums[j] not in s:
                    l.append(nums[j])
                    s.add(nums[j])
                    p = dfs(l,s)
                    l.pop()
                    s.remove(nums[j])

        dfs([],set())
        return res
            


