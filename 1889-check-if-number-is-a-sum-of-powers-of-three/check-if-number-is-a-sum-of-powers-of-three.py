class Solution:
    
    def helper(self,n,power):
        if n==0:
            return True
        if 3**power>n:
            return False
        
        keep=self.helper(n-(3**power),power+1)
        skip=self.helper(n,power+1)
        if keep or skip:
            return True
        return False
    def checkPowersOfThree(self, n: int) -> bool:
        # while (n>0):
        #     if n%3>1:
        #         return False
        #     n=n//3
        # return True

        return self.helper(n,0)