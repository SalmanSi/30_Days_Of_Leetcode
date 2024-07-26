class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        # edges.sort(key=lambda x: x[0])

        graph=[[inf for i in range(n)] for i in range(n)]
        count=[0 for i in range(n)]
        for edge in edges:
            start,end,weight=edge
            graph[start][end]=weight
            graph[end][start]=weight
        

        for i in range(n):# going through this node
            for j in range(n): # from this node
                for k in range(n): # to this node
                    if j==k: 
                        continue
                    if graph[j][k] > graph[j][i]+graph[i][k]:
                        graph[j][k]=graph[j][i]+graph[i][k]
                    if i == n-1:
                        if graph[j][k]<= distanceThreshold:
                            count[j]+=1


        smallest=min(count)
        ans=0
        for i in range(n):
            if count[i]==smallest and i > ans:
                ans=i
        return ans 

