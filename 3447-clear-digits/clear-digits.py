class Solution:
    def clearDigits(self, s: str) -> str:
        ans=[]

        for i in range(len(s)):
            if ord(s[i])<=57 and ord(s[i])>=48:
                ans.pop()
            else:
                ans.append(s[i])
        ans=''.join(ans)
        print(ans)
        return ans