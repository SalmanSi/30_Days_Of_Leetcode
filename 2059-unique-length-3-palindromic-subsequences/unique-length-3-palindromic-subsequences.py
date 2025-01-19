class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        all_chars=set(s)
        ans=0
        for c in all_chars:
            start_idx=-1
            end_idx=-1


            for i in range(len(s)):
                if s[i]==c:
                    if start_idx==-1:
                        start_idx=i 
                    end_idx=i
            if start_idx==-1 or start_idx==end_idx:
                continue
            myset=set(s[start_idx+1:end_idx])
            ans+=len(myset)
        return ans   
            



        ## my solution
        # left_char_set=set()
        # r=len(s)-1
        # l=0
        # ans=0
        # for L in range(len(s)-2):
        #     if s[L] in left_char_set:
        #         continue
        #     l=L
        #     r=len(s)-1
        #     while(r-l>1 and s[l]!=s[r]):
        #         r-=1# come from the right to find the rightmost occurence of the char
            
            
            
        #     myset=set(s[l+1:r])
        #     left_char_set.add(s[L])
        #     ans+=len(myset)
        # return ans
        