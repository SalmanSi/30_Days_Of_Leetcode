class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans=0
        curr=1
        length=len(nums)
        i=0
        incr=False
        
        while i<length-1:
            if nums[i]==nums[i+1]:
                ans=max(ans,curr)
                curr=1
            elif incr:
                if nums[i]>nums[i+1]:
                    ans=max(ans,curr)
                    curr=1
                    incr=False
                    i-=1
                else:
                    curr+=1
            elif not incr:
                if nums[i]<nums[i+1]:
                    ans=max(ans,curr)
                    curr=1
                    incr=True
                    i-=1
                else:
                    curr+=1
            i+=1
        ans=max(ans,curr)
        return ans