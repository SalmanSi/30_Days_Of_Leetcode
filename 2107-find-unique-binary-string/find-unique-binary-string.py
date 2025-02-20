class Solution:


    def getAllString(self,n:int,nums: set, cur:str) -> None:
        if len(cur)==n:
            if cur not in nums:
                return cur
            else:
                return 'null'
        if len(cur)<n:     
            ans= self.getAllString(n,nums,cur+'0')
            if ans !="null":
                return ans
            ans= self.getAllString(n,nums,cur+'1')
            if ans!="null":
                return ans
        return 'null'

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums[0])
        nums=set(nums)
        

        ans=self.getAllString(n,nums,"")
        return ans