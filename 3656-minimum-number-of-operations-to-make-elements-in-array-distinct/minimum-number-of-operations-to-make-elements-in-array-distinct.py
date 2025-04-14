class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans=0
        i=0
        
        myset=set()
        for ptr in range(len(nums)-1,i,-1):
            while nums[ptr] in (nums[i:ptr]):
                ans+=1
                i+=3
        return ans
            