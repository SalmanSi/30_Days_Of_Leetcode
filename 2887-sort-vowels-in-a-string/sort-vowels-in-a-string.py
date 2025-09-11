class Solution:
    def sortVowels(self, s: str) -> str:
        vowels={"a","e","i","o","u","A","E","I","O","U"}
        my_list=[]
        for c in s:
            if c in vowels:
                my_list.append(c)
        s=list(s)
        my_list.sort()
        i=0
        for idx in range(len(s)):
            if s[idx] in vowels:
                s[idx]=my_list[i]
                i+=1
        return "".join(s)

