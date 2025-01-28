class Solution:

    def BFS(self,grid,r,c,rows,cols):
        tree_sum=grid[r][c]
        grid[r][c]=-1
        q=deque()
        q.append((r,c))
        while q:
            r,c=q.popleft()

            if r>0:
                if grid[r-1][c]>0:
                    tree_sum+=grid[r-1][c]
                    grid[r-1][c]=-1
                    q.append((r-1,c))
            if r<rows-1 :
                if grid[r+1][c]>0:
                    tree_sum+=grid[r+1][c]
                    grid[r+1][c]=-1
                    q.append((r+1,c))
            if c>0 :
                if grid[r][c-1]>0 :
                    tree_sum+=grid[r][c-1]
                    grid[r][c-1]=-1
                    q.append((r,c-1))
            if c<cols-1:
                if grid[r][c+1]>0:
                    tree_sum+=grid[r][c+1]
                    grid[r][c+1]=-1
                    q.append((r,c+1)) 
            print(tree_sum)   
            print(q)       
        return tree_sum
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ans=0
        rows=len(grid)
        cols=len(grid[0])


        for r in range(rows):
            for c in range(cols):
                if grid[r][c]>0: # this is unvisited
                    ans=max(ans,self.BFS(grid,r,c,rows,cols))


        return ans
