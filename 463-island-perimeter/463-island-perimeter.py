class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        rows, cols = len(grid), len(grid[0])
        self.count = 0
        visit = set()
        
        def bfs(r,c):
            print("inside bfs for: ",r,c)
            visit.add((r,c))
            directions = [[-1,0],[0,-1],[1,0],[0,1]]
            for dir in directions:
                rw, cl = r+dir[0], c+dir[1]
                if rw not in range(rows):
                    self.count += 1
                if cl not in range(cols):
                    self.count += 1
                if rw in range(rows) and cl in range(cols) and grid[rw][cl]==0:
                    self.count += 1
                if rw in range(rows) and cl in range(cols) and grid[rw][cl]==1 and (rw,cl) not in visit:
                    bfs(rw,cl)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1 and (row,col) not in visit:
                    bfs(row,col)
                    
                
            
                    
        return self.count
        