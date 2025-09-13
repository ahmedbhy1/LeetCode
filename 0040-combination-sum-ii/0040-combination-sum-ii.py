class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        I = []
        res = []
        nums = 51 * [0]
        for i in candidates:
            nums[i] +=1
        print(nums[0:10])
        def dfs(indx,target,nums):
            
            if target == 0 and indx == 50:
                res.append(I.copy())

            if indx > 50 or target < 0:
                return


            if nums[indx] > 0:
                nums[indx] -= 1
                I.append(indx)
                dfs(indx,target-indx,nums.copy())
                I.pop()

            dfs(indx+1 , target,nums.copy())
        
        dfs(0,target,nums.copy())
        return res