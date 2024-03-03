class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        # Graph construction
        courses = {i: [] for i in range(numCourses)}
        for course, prerequisite in prerequisites:
            courses[course].append(prerequisite)

        visited = set() # Tracks courses during the current path of DFS
        cleared = set() # Tracks courses that have been fully explored and confirmed not to be part of a cycle

        def hasCycle(course: int) -> bool:
            if course in cleared:
                return False
            if course in visited:
                return True

            visited.add(course)

            for prereq in courses[course]:
                if (hasCycle(prereq)):
                    return True

            visited.remove(course)
            cleared.add(course)

            return False


        for i in range(numCourses):
            if hasCycle(i):
                return False

        return True
