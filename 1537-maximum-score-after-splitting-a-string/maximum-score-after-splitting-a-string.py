class Solution:
    def maxScore(self, s: str) -> int:
        max_=0
        for i in range(0,len(s)-1):
            score=0
            for j in range(i+1):
                if s[j]=='0':
                    score+=1
            for j in range(i+1,len(s)):
                if s[j]=='1':
                    score+=1
            max_=max(score,max_)
        return max_
