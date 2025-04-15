class Solution:
    def isValid(self, s: str) -> bool:
        mystr=list(s)
        stack=[]
        for c in mystr:
            if len(stack)==0:
                stack.append(c)
            elif c =='{' or c=='(' or c=='[':
                stack.append(c)
            elif c==')' and stack[-1]!='(' or c=='}' and stack[-1]!='{' or c==']' and stack[-1]!='[' :
                return False
            else:
                stack.pop()
            
        return  len(stack)<=0
