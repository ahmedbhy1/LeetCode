class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        L = [0] * 20002
        n = len(nums)
        for i in range(n):
            nums[i] += 10000
        
        L[nums[0]] = 1
        for i in range(1,n):
            maxx = 1
            for x in range(i):
                j = nums[x]
                if j < nums[i]:
                    maxx = max(maxx , L[j]+1)
            L[nums[i]] = maxx
        print(L[10000:10011])
        
        return max(L)