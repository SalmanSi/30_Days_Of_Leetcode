class Solution:


    def getAllString(self,n:int,nums: set,myset:set, cur:str) -> None:
        if len(cur)==n:
            if cur not in nums:
                myset.add(cur)
            return
        if len(cur)<n:     
            self.getAllString(n,nums,myset,cur+'0')
            self.getAllString(n,nums,myset,cur+'1')
        return      

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums[0])
        nums=set(nums)
        myset=set()

        self.getAllString(n,nums,myset,"")
        for x in myset:
            return x