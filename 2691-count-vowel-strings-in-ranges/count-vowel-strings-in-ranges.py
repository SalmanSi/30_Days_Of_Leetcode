class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        words_bool=[]
        vowels={'a','e','i','o','u'}
        comm_freq=[]
        for word in words:
            if (word[0] in vowels) and (word[-1] in vowels):
                words_bool.append(1)
            else:
                words_bool.append(0)
            if len(comm_freq)<1:
                comm_freq.append(words_bool[-1])
            else:
                comm_freq.append(words_bool[-1]+comm_freq[-1])#make a commutaltice freq count    array
            
        ans=[]
        for idx,q in enumerate(queries):
            ans.append(words_bool[q[0]])
            ans[-1]+=comm_freq[q[1]]-comm_freq[q[0]]
        return ans

        