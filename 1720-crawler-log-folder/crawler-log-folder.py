class Solution:
    def minOperations(self, logs: List[str]) -> int:
        dist=0
        for log in logs:
            if log=="../":
                if dist>0:
                    dist-=1
                else:
                    continue
            elif log=="./":
                continue
            else:
                dist+=1
        return dist