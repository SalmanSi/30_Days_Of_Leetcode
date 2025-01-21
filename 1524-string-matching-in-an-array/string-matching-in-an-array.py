class Solution:
    def isSubStringOf(self, main:str,sub:str) -> bool:
        sub_len=len(sub)
        main_len=len(main)
        for startIndex in range(main_len):
            if main[startIndex:startIndex+sub_len]==sub:
                return True
        return False

    def stringMatching(self, words: List[str]) -> List[str]:
        ans=[]
        for cur_word in words:
            for other_word in words:
                if cur_word==other_word:
                    continue
                if self.isSubStringOf(other_word,cur_word):
                    ans.append(cur_word)
                    break
        return ans



  