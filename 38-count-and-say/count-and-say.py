class Solution:
    def rle(self,cur):
        last=cur[0]
        count=1
        new=''
        for i in range(len(cur)-1):
            if cur[i]!=cur[i+1]:
                new+=str(count)
                new+=str(cur[i])
                count=1
            else:
                count+=1
        new+=str(count)
        new+=str(cur[-1])
        return new



    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        cur=self.countAndSay(n-1)
        new=self.rle(cur)
        return new