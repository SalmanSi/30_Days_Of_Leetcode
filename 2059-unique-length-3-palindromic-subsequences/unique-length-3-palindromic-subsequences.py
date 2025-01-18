class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        myset=set()
        left_char_set=set()
        r=len(s)-1
        l=0
        for L in range(len(s)-2):
            if s[L] in left_char_set:
                continue
            l=L
            r=len(s)-1
            while(r-l>1 and s[l]!=s[r]):
                r-=1
     
            for i in range(l+1,r):
                myset.add(str(s[l]+s[i]+s[r]))
            left_char_set.add(s[L])
        return len(myset)
        