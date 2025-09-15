class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ans=0
        words=text.split(" ")
        for w in words:
            for c in brokenLetters:
                if c in w:
                    ans+=1
                    break
        return (len(words)-ans)