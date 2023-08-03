class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preq = defaultdict(list)
        for cor, pre in prerequisites:
            preq[cor].append(pre)
        
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if preq[course] == []:
                return True
            visited.add(course)
            for pre in preq[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            preq[course] = []
            return True
            
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True