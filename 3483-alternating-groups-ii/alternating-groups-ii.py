class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        # ans=0
        # for i in range(len(colors)):
        #     ans+=1
        #     for j in range(i+1,i+k):
        #         j=j%len(colors)
        #         if colors[j]==colors[j-1]:
        #             ans-=1
        #             break
        # return ans
        size=len(colors)
        colors.extend(colors[:k-1])
        ans=0
        left=0
        for right in range(1,size+k-1):
            if colors[right-1]==colors[right]:
                left=right
            if right-left+1==k:
                ans+=1
                left+=1
        print(ans)
        return ans
            
                