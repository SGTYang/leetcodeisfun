class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = defaultdict(list)
        res = []
        visited, cycle = set(), set()
        for cor, pre in prerequisites:
            prereq[cor].append(pre)
            
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)
            
            for cor in prereq[course]:
                if not dfs(cor):
                    return False
            cycle.remove(course)
            visited.add(course)
            res.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res