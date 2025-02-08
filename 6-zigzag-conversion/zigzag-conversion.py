class Solution:
    def convert(self, s: str, numRows: int) -> str:
        cur=0
        ans=[]
        s=list(s)
        i=0
        while i<len(s):
            col=[]
            if cur==0:
                col=s[i:i+numRows]
                i+=numRows
                cur=max(0,numRows-2)
            else:
                for j in range(numRows):
                    if cur==j:
                        col.append(s[i])
                    else:
                        col.append(" ")
                i+=1
                cur-=1
            ans.append(col)

        st=[]
        for c in range(len(ans[0])):
            for r in range(len(ans)):
                if c< len(ans[r]):
                    if ans[r][c]!=" ":
                        st.append(ans[r][c])
                else:
                    break
        
        return ("").join(st)