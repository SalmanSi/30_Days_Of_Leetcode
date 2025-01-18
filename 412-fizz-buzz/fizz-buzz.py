class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        ans=[]

        for i in range(n):
            word=""
            if (i+1)%3==0:
                word+="Fizz"
            if (i+1)%5==0:
                word+="Buzz"
            if len(word)==0:
                word+=str(i+1)    
            ans.append(word)
        
        return ans
        