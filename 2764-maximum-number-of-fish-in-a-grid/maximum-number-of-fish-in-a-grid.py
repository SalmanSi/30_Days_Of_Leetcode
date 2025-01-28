class Solution:

    def BFS(self,visited,grid,r,c,rows,cols):
        tree_sum=0
        q=deque()
        q.append((r,c))
        while q:
            r,c=q.popleft()
            visited[r][c]=-1
            tree_sum+=grid[r][c]
            if r>0:
                if grid[r-1][c]!=0 and visited[r-1][c]==0:
                    visited[r-1][c]=-1
                    q.append((r-1,c))
            if r<rows-1 :
                if grid[r+1][c]!=0 and visited[r+1][c]==0:
                    visited[r+1][c]=-1
                    q.append((r+1,c))
            if c>0 :
                if grid[r][c-1]!=0 and visited[r][c-1]==0:
                    visited[r][c-1]=-1
                    q.append((r,c-1))
            if c<cols-1:
                if grid[r][c+1]!=0 and visited[r][c+1]==0:
                    visited[r][c+1]=-1
                    q.append((r,c+1)) 
            print(tree_sum)   
            print(q)       
        return tree_sum
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ans=0
        rows=len(grid)
        cols=len(grid[0])
        visited=[[-1 for i in range(cols)] for i in range (rows)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]>0:
                    visited[r][c]=0
        

        for r in range(rows):
            for c in range(cols):
                if visited[r][c]==0: # this is unvisited
                    ans=max(ans,self.BFS(visited,grid,r,c,rows,cols))


        return ans
