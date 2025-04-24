class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        ans=[]
        for r in range(len(box)):
            hashcount=0
            dashcount=0
            rnew=[]
            for c in range(len(box[0])):
                if box[r][c]=='#':
                    hashcount+=1
                elif box[r][c]=='.':
                    dashcount+=1
                else:
                    while dashcount>0:
                        rnew.append('.')
                        dashcount-=1
                    while hashcount>0:
                        rnew.append('#')
                        hashcount-=1
                    rnew.append('*')
            while dashcount>0:
                rnew.append('.')
                dashcount-=1
            while hashcount>0:
                rnew.append('#')
                hashcount-=1
            ans.append(rnew)
        final=[]
        for col in range(len(box[0])):
            r=[]
            for row in range(len(box)-1,-1,-1):
                r.append(ans[row][col])
            final.append(r)
        return final