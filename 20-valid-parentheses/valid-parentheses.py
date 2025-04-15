class Solution:
    def isValid(self, s: str) -> bool:
        mymap={')':'(','}':'{',']':'['}
        stack=[]
        for i in range(len(s)):
            if stack:
                if s[i] in mymap:
                    if mymap[s[i]]!=stack.pop():
                        return False
                    continue
            stack.append(s[i])
        return not stack
            

