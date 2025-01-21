class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words_joined=' '.join(words)
        ans=[]
        for word in words:
            if words_joined.count(word)>1:
                ans.append(word)
        return ans

        # n=len(words)
        # words.sort(key=len)
        # ans=[]

        # for i in range(n):
        #     for j in range(i+1,n):
        #         if words[i] in words[j]:
        #             ans.append(words[i])
        #             break
        # return ans