class Solution:
    # def checkUnique(self,nums,start):
    #     myset=set()
    #     for num in nums[start:]:
    #         if num in myset:
    #             return False
    #         myset.add(num)
    #     return True 
    def minimumOperations(self, nums: List[int]) -> int:
        # ans=0
        # for i in range(0,len(nums),3):
        #     if self.checkUnique(nums,i):
        #         return ans
        #     ans+=1
        # return ans

        # optimized solution
        seen=[0]*101
        for i in range(len(nums)-1,-1,-1):
            if seen[nums[i]]:
                return (i//3 +1)
            else:
                seen[nums[i]]=1
        return 0