from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        req = {i: [] for i in range(numCourses)}
        # req[course] = list of courses that become available after completing 'course'

        for prereq in prerequisites:
            req[prereq[1]].append(prereq[0])
            indegree[prereq[0]] += 1

        result = []
        q = deque()

        for i, el in enumerate(indegree):
            if el == 0:   
                q.append(i)
                
        # queue contains courses with no prerequisites - start from them
        while q:
            course = q.popleft()
            result.append(course)

            for nei in req[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return result if len(result) == numCourses else []