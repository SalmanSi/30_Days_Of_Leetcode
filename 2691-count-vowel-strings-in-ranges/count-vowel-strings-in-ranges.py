class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        vowels={'a','e','i','o','u'}
        comm_freq=[0]*len(words)
        Sum=0
        for i,word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                Sum+=1
            comm_freq[i]=Sum
            
        ans=[0]*len(queries)
        for idx,q in enumerate(queries):
            if q[0]==0:
                ans[idx]=(comm_freq[q[1]]-0)
            else:
                ans[idx]=(comm_freq[q[1]]-comm_freq[q[0]-1])

        return ans

        