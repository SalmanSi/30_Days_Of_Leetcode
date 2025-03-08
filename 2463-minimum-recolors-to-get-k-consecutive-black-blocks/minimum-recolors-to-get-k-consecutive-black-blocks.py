class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        # minOps=len(blocks)
        # blocks=list(blocks)

        # for i in range(len(blocks)-k+1):
        #     current_ops=0
        #     for j in range(i,i+k):
        #         if blocks[j]=='W':
        #             current_ops+=1
        #     minOps=min(minOps,current_ops)

        # return minOps

        minOps=len(blocks)
        blocks=list(blocks)

        dp=[0]*(len(blocks)+1)
        cur=0
    
        for i in range(len(blocks)):
            if blocks[i]=='W':
                cur+=1
            dp[i]=cur 


        for i in range(len(blocks)-k+1):
            minOps=min(minOps,(dp[i+k-1]-dp[i-1]))

        print(dp)
        return minOps