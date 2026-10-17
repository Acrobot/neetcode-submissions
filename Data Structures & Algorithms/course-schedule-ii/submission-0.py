class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = defaultdict(list[int])
        indegrees = defaultdict(int)

        for p in prerequisites:
            edges[p[-1]].append(p[0])
            indegrees[p[0]] += 1

        zero_indegrees = deque(
            course for course in range(numCourses)
            if indegrees[course] == 0
        )

        returned = []

        while zero_indegrees:
            completed = zero_indegrees.pop()

            returned.append(completed)

            for p in edges[completed]:
                indegrees[p] -= 1

                if indegrees[p] == 0:
                    zero_indegrees.appendleft(p)

        return returned if len(returned) == numCourses else []