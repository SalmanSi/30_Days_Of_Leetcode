class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        final_shifts=[0]*len(s)

        for shift in shifts:
            start=shift[0]
            end=shift[1]
            forward=shift[2]

            if forward:
                final_shifts[start]+=1
                if end !=len(final_shifts)-1:
                    final_shifts[end+1]-=1
            else:
                final_shifts[start]-=1
                if end !=len(final_shifts)-1:
                    final_shifts[end+1]+=1
                

        for i in range(1,len(final_shifts)):
            final_shifts[i]+=final_shifts[i-1]
        ans=list(s)

        for i in range(len(s)):
            if final_shifts[i]==0:
                continue
            ans[i]=chr(ord(ans[i])+(final_shifts[i]%26))
            if ans[i]>'z':
                ans[i]=chr(ord(ans[i])-26)
            elif ans[i]<'a':
                ans[i]=chr(ord(ans[i])+26)
        ans=''.join(ans)
        return ans
        
