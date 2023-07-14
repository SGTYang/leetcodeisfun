class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {c:[] for c in range(numCourses)}
        
        for cor, pre in prerequisites:
            prereq[cor].append(pre)
        
        visited = set()
        
        def dfs(course):
            if course in visited:
                return False
            if prereq[course] == []:
                return True
            
            visited.add(course)
            
            for pre in prereq[course]:
                if not dfs(pre):
                    return False
                
            visited.remove(course)
            prereq[course] = []
            
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            