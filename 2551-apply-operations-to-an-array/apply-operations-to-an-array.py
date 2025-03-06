class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        
        ans=[]
        zeros=[]
        for i in range(len(nums)):
            if nums[i]!=0:
                ans.append(nums[i])
            else:
                zeros.append(0)
        ans.extend(zeros)        
        return ans
