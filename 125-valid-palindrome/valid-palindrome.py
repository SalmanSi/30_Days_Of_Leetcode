class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s=s.lower()
        # alphabets={'a','b','c','d','e','f'
        # ,'g','h','i','j','k','l','m','n','o','p','q' ,'r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0'  }
        # mylist=[]
        # for ch in s:
        #     if ch in alphabets:
        #         mylist.append(ch)
        
        # size=len(mylist)
        # print(mylist)
        # for i in range(0,size//2):
        #     if mylist[i]!=mylist[-i-1]:
        #         print(i)
        #         return False
        # return True

        s=''.join(c.lower() for c in s if c.isalnum() )
        left=0
        right=len(s)-1
        while left<right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True