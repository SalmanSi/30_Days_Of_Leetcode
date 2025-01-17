class Solution:
    def maxScore(self, s: str) -> int:
        ones=s.count('1')
        zeros=0
        score=0
        for i in range(len(s)-1):
            if s[i]=='1':
                ones-=1
            else:
                zeros+=1
            score=max(score,ones+zeros)
        return score