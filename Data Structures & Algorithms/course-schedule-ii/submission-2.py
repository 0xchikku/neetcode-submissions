class Solution:
    # time - O(V+E), space - O(V+E)
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = {}
        for i in range(numCourses):
            courses[i] = []
        for prerequisite in prerequisites:
            courses[prerequisite[0]].append(prerequisite[1])
        
        res = []
        inProgress = set()
        completed = set()
        def canComplete(course):
            if course in inProgress:
                return False
            
            if course in completed:
                return True
            
            inProgress.add(course)
            for prerequisite in courses[course]:
                if not canComplete(prerequisite):
                    return False
                    
            res.append(course)
            inProgress.remove(course)
            completed.add(course)
            return True
        

        for i in range(numCourses):
            if not canComplete(i):
                return []
        return res