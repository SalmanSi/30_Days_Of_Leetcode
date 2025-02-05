class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        index=[]
        c=0
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                index.append(i)
                c+=1
                if c>2:
                    return False
        if c==0:
            return True  
        if c==1:
            return False
        if s1[index[0]]==s2[index[1]] and s2[index[0]]==s1[index[1]]:
            return True
        return False