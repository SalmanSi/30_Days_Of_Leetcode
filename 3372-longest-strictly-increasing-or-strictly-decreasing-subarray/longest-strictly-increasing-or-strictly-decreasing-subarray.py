class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        incLen=decLen=maxLen=1
        for i in range(len(nums)-1):
            if nums[i+1]>nums[i]:
                incLen+=1
                decLen=1
            elif nums[i+1]<nums[i]:
                decLen+=1
                incLen=1
            else:
                decLen=incLen=1
            maxLen=max(decLen,incLen,maxLen)

        return maxLen
        # ans=0
        # curr=1
        # length=len(nums)
        # i=0
        # incr=False
        
        # while i<length-1:
        #     if nums[i]==nums[i+1]:
        #         ans=max(ans,curr)
        #         curr=1
        #     elif incr:
        #         if nums[i]>nums[i+1]:
        #             ans=max(ans,curr)
        #             curr=1
        #             incr=False
        #             i-=1
        #         else:
        #             curr+=1
        #     elif not incr:
        #         if nums[i]<nums[i+1]:
        #             ans=max(ans,curr)
        #             curr=1
        #             incr=True
        #             i-=1
        #         else:
        #             curr+=1
        #     i+=1
        # ans=max(ans,curr)
        # return ans