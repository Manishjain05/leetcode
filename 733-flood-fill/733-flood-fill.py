class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        rows,cols = len(image),len(image[0])
        visit=set()
        val = image[sr][sc]
        
        def bfs(r,c):
            
            directions = [[-1,0],[0,-1],[1,0],[0,1]]
            for dir in directions:
                rw, cl = r+dir[0], c+dir[1]
                if rw in range(rows) and cl in range(cols) and image[rw][cl]==val and (rw,cl) not in visit:
                    image[rw][cl]=color
                    visit.add((rw,cl))
                    bfs(rw,cl)
            
            
            
        image[sr][sc] = color
        visit.add((sr,sc))
        bfs(sr,sc)
        
        return image
        