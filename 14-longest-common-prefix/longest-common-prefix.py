class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        all_prefixes=[]
        for s in strs:
            s_len=len(s)
            for i in range(1,s_len+1):
                all_prefixes.append(s[:i])
        freq=dict(Counter(all_prefixes))
        sorted_dict=sorted(freq.items(),key= lambda x:(-x[1],-len(x[0])) )
        # if len(sorted_dict)==0:
        #     return ""
        # ans=sorted_dict[0]
        # if ans[1]>1:
        #     return ans[0]
        # else:
        #     return ""
        ans=""
        for item in sorted_dict:
            k,v=item
            if v==len(strs) and len(k)>len(ans):
                ans=k
        return ans