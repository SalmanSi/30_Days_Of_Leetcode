class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        #1. first seprate the 2 islands in a dict
        #2. then, copmute distances -1 and return smallest
        r=len(grid)
        c=len(grid[0])

        
        visited=set()
        q=deque()
        flag=False
        for i in range (r):
            for j in range (c):
                if grid[i][j]==1:
                    q.append((i,j))
                    flag=True
                    break
            if flag:
                break
        i_dict={1:[],2: []}
        while q:
            cur=q.popleft()
            if cur in visited:
                continue
            visited.add(cur)
            x,y=cur
            if grid[x][y]==1:
                i_dict[1].append((x,y))
            #chk right
            if y+1<c and grid[x][y+1]==1:
                q.append((x,y+1))
            #left
            if y-1>=0 and grid[x][y-1]==1:
                q.append((x,y-1))
            if x+1<r and grid[x+1][y]==1:
                q.append((x+1,y))
            if x-1>=0 and grid[x-1][y]==1:
                q.append((x-1,y))
        for i in range(r):
            for j in range(c):
                if (i,j) not in visited and grid[i][j]==1:
                    i_dict[2].append((i,j))

        i1=i_dict[1]
        i2=i_dict[2]
        dist=inf
        for t1 in i1:
            for t2 in i2:
                cur_dist=abs(t2[0]-t1[0])+abs(t2[1]-t1[1])-1
                dist=min(dist,cur_dist)
        return dist
        print(i_dict)