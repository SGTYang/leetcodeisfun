class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = defaultdict(list)
        for cor, pre in prerequisites:
            prereq[cor].append(pre)
        
        visited = set()
        
        def dfs(course):
            if course in visited:
                return False
            if prereq[course] == []:
                return True
            visited.add(course)
            for cor in prereq[course]:
                if not dfs(cor):
                    return False
            prereq[course] = []
            visited.remove(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True