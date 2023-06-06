class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        count = defaultdict(list)
        
        for pre in prerequisites:
            count[pre[0]].append(pre[1])
        
        def dfs(course):
            if course in visited:
                return False
            if count[course] == []:
                return True
            
            visited.add(course)
            for c in count[course]:
                if not dfs(c):
                    return False
            visited.remove(course)
            count[course] = []
            
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True