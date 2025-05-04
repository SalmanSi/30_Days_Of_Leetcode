class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        ans=0
        dom_count=defaultdict(int)
        for i in range(len(dominoes)):
            dominoes[i].sort()
            a=dominoes[i][0]
            b=dominoes[i][1]
            ans+=dom_count[(a,b)]
            dom_count[(a,b)]+=1
            
        return ans
    