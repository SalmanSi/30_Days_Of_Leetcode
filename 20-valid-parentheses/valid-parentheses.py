class Solution:
    def isValid(self, s: str) -> bool:
        mymap={')':'(','}':'{',']':'['}
        stack=[]
        for char in s:
            if char in mymap.values():
                stack.append(char)
            else:
                if not stack or mymap[char]!=stack.pop():
                    return False
        return not stack
            

