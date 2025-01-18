class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left_char_set=set()
        r=len(s)-1
        l=0
        ans=0
        for L in range(len(s)-2):
            if s[L] in left_char_set:
                continue
            l=L
            r=len(s)-1
            while(r-l>1 and s[l]!=s[r]):
                r-=1# come from the right to find the rightmost occurence of the char
            
            
            
            myset=set(s[l+1:r])
            left_char_set.add(s[L])
            ans+=len(myset)
        return ans
        