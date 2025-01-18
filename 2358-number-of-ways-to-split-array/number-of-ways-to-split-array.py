class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        sumRt=sum(nums) # sum of all elements to the right of i

        sumLt=0 # sum of all elements to the left of i
        ans=0
        for i in range(len(nums)-1):
            sumLt+=nums[i]
            sumRt-=nums[i]
            if sumLt>=sumRt:
                ans+=1
        return ans