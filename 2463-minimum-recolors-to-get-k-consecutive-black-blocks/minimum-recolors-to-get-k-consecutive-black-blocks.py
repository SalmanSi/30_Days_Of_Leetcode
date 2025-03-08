class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        minOps=len(blocks)
        blocks=list(blocks)

        for i in range(len(blocks)-k+1):
            current_ops=0
            for j in range(i,i+k):
                if blocks[j]=='W':
                    current_ops+=1
            minOps=min(minOps,current_ops)

        return minOps