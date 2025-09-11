class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=[]
        min_len=inf
        for s in strs:
            min_len=min(min_len,len(s))
        for i in range(min_len):
            for idx in range(len(strs)-1):
                if strs[idx][i]!=strs[idx+1][i]:
                    return "".join(ans)
            ans.append(strs[0][i])
        return "".join(ans)
