class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c:[] for c in range(numCourses)}
        
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
        visited, cycle = set(), set()
        output = []
        
        def dfs(crs):
            if crs in visited:
                return True
            if crs in cycle:
                return False
            
            cycle.add(crs)
            
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return output