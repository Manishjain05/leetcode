class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        preMap = {i:[] for i in range(numCourses)}
        print(preMap)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        print(preMap)
        visitedSet = set()
        print(visitedSet)
        
        def dfs(crs):
            if crs in visitedSet:
                print("infinite loop")
                return False
            if preMap[crs] == []:
                print("no pre-req")
                return True
            visitedSet.add(crs)
            print("added in visited")
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visitedSet.remove(crs)
            print("removed from visited")
            preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        
        return True
                
            
            
        
        
        