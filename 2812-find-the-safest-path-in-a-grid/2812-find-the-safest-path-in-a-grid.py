class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        """
        find the safest path in the grid

        safness factor is minimum distance manhattan distance betweeen the 

        cell and the theif   maximise the safness factor 


        is it reverse bfs Ig so 
        """
        m=len(grid)
        n=len(grid[0])
        visited=[[float('inf')]*(n) for _ in range(m)]
        q=deque()
        for i in range(m):
            for  j in  range(n):
                if grid[i][j]==1:
                    visited[i][j]=0
                    q.append((0,i,j))
        while q:
            time,x,y=q.popleft()
            if visited[x][y]<time:
                continue 
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                if 0<=x+dx<m and 0<=y+dy<n:
                    if visited[x+dx][y+dy]>time+1:
                        visited[x+dx][y+dy]=time+1
                        q.append((time+1,x+dx,y+dy))
        # for row in visited:
        #     print(*row)
        #now via moving along the visited grid our minimum Should be maximum 


        #How will u do that is it Binary search 
        #if i can reach for x 
        #than i can reach for x-1 
        #yes it si monotimic 
        


        def find(val):
            q=deque()
            vis=[[False]*(n) for _ in range(m)]
            # print(visited)
            if visited[0][0]>=val:
                q.append((0,0))
            while q:
                x,y=q.popleft()
                if x==m-1 and y==n-1:
                    return True
                vis[x][y]=True
                for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    if 0<=x+dx<m and 0<=y+dy<n:
                        if not vis[x+dx][y+dy] and visited[x+dx][y+dy]>=val:
                            vis[x+dx][y+dy]=True
                            q.append((x+dx,y+dy))
            return False
        low=0
        high=m+n
        ans=-1
        while low<=high:
            mid=(low+high)>>1
            if find(mid):
                ans=mid
                low=mid+1
            else:
                high=mid-1
        # print(find(0))
        return ans