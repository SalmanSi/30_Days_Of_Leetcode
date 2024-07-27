class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        
        graph=[[inf for i in range(26)] for j in range(26)]

        n=len(cost)
        # populate the graph
        for i in range(n):
            row=ord(original[i])-ord('a')
            col=ord(changed[i])-ord('a')
            if graph[row][col]>cost[i]:
                graph[row][col]=cost[i]

        # find least cost of all sources to all ends 
        # using floyd warshall algorithm
        for i in range(26):# intermediate node
            for j in range(26):#source node
                for k in range(26):#end node
                    if j==k:
                        graph[j][k]=0 # very important
                        continue
                    if graph[j][k]>graph[j][i]+graph[i][k]:
                        graph[j][k]=graph[j][i]+graph[i][k]
                    
        cost=0
        n=len(source)
        for i in range(n):
            row=ord(source[i])-ord('a')
            col=ord(target[i])-ord('a')
            if graph[row][col]==inf:
                return -1
            cost+=graph[row][col]
            
        return cost




        # source_nodes=list(set(original))
        # end_nodes=list(set(changed))

        # source_nodes.sort()
        # for i in range(len(source_nodes))
        # end_nodes.sort()
        # graph=[[inf for i in range(len(end_nodes))] for j in range(len(source_nodes))]
        # print(f"rows={len(source_nodes)}")
        # print(f"rows={len(end_nodes)}")
        # n=len(original)
        # for i in range(n):
        #     print(f"letter:{original[i]}  row:{ord(original[i])-97}" )
        #     print(f"letter:{changed[i]}  col:{ord(changed[i])-97}" )
            
        #     # graph[ord(original[i])-97][ord(changed[i])-97]=cost[i]
            
        # print(graph)
        # # print(source_nodes)
        # # print(end_nodes)
        # return 0