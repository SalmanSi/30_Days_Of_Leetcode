class Solution:
    def isPrefixAndSuffix(self,str1,str2):
        l1=len(str1)
        l2=len(str2)
        if l1>l2:
            return False
        for i in range(l1):
            if str1[i]!=str2[i]:
                return False
            j=l1-i-1
            k=l2-i-1
            if str1[j]!=str2[k]:
                return False
        return True
    
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if self.isPrefixAndSuffix(words[i],words[j]):
                    ans+=1
        return ans
    
