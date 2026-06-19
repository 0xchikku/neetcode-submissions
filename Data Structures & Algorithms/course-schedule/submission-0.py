class Solution:
    #  time - O(V + E), space - O(V + E)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        for prerequisite in prerequisites:
            graph[prerequisite[0]].append(prerequisite[1])
        
        inProgess = set()
        completed = set()

        def canComplete(course):
            if course in inProgess:
                return False
            if course in completed:
                return True
            
            inProgess.add(course)
            for prerequisite in graph[course]:
                if not canComplete(prerequisite):
                    inProgess.remove(course)
                    return False
            
            inProgess.remove(course)
            completed.add(course)
            return True
        
        for i in range(numCourses):
            if not canComplete(i):
                return False
        return True
            