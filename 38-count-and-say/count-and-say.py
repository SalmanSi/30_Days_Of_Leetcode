class Solution:
    def rle(self,cur):
        last=cur[0]
        count=1
        new=[]
        for c in cur[1:]:
            if c!=last:
                new.append(count)
                new.append(last)
                last=c
                count=1
            else:
                count+=1
        new.append(count)
        new.append(last)
        return ''.join(map(str,new))



    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        cur=self.countAndSay(n-1)
        new=self.rle(cur)
        return new