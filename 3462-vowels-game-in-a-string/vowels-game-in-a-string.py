class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels="aeiou"
        count=0
        for c in s:
            if c in vowels:
                count+=1
        if count==0:
            return False
        else:
            return True