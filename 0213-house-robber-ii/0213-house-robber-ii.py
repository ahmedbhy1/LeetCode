class Solution:
    def rob(self, nums: list[int]) -> int:
        nums2 = copy.deepcopy(nums)
        x = nums2.pop(0)
        nums2 = nums2 + [x]
        n = len(nums2)
        for i in range(2,n):
            if i>2:
                nums2[i] += max(nums2[i-2], nums2[i-3])
                nums[i] += max(nums[i-2], nums[i-3])
            else:
                nums2[i] += nums2[i-2]
                nums[i] += nums[i-2]

        if n >= 3:
            return max(max(nums2[n-2], nums2[n-3]),max(nums[n-2], nums[n-3]))
        else:
            return max(nums2[n-2], nums[n-2])