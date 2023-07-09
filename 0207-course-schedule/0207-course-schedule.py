class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {c:[] for c in range(numCourses)}
        
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
        visited = set()
        
        def dfs(crs):
            if crs in visited:
                return False
            if prereq[crs] == []:
                return True
            
            visited.add(crs)
            
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            
            visited.remove(crs)
            prereq[crs] = []
            
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True