class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]

        for ch in s:
            my_string=""
            if ch!=')':
                stack.append(ch)
            else:
                while stack[-1]!="(":
                    my_string+=stack.pop()
                stack.pop()
                for i_ch in my_string:
                    stack.append(i_ch)
                
                    
        my_string=""
        for item in stack:
            my_string+=item
        return my_string