class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        ans=[]

        for i in range(n):
            word=str(i+1)
            flag=True
            if (i+1)%3==0:
                word="Fizz"
                flag=False
            if (i+1)%5==0:
                if flag:
                    word="Buzz"
                else:
                    word+="Buzz"
            ans.append(word)
            print(word)
        
        return ans
        