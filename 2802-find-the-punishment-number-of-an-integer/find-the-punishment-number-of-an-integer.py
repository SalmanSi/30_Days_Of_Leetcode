class Solution:
    def canPartition(self,num,target):
        if target<0 or num<target:
            return False
        
        if num==target:
            return True
        
        return (
            self.canPartition(num//10,target-num%10)
            or 
            self.canPartition(num//100,target-num%100)
            or 
            self.canPartition(num//1000,target-num%1000)
        )


    def punishmentNumber(self, n: int) -> int:
        ans=0
        for i in range(1,n+1):
            sq=i*i
            if self.canPartition(sq,i):
                ans+=sq
        return ans
