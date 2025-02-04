class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans=0
        cur=nums[0]

        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                cur+=nums[i]
            else:
                ans=max(ans,cur)
                cur=nums[i]
        ans=max(ans,cur)
        return ans
