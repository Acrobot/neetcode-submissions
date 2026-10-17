class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = defaultdict(list[int])
        indegrees = defaultdict(int)

        for p in prerequisites:
            edges[p[-1]].append(p[0])
            indegrees[p[0]] += 1

        zero_indegree = deque(
            course for course in range(numCourses)
            if indegrees[course] == 0
        )

        completed_count = 0

        while zero_indegree:
            completed = zero_indegree.pop()
            completed_count += 1

            for e in edges[completed]:
                indegrees[e] -= 1

                if indegrees[e] == 0:
                    zero_indegree.appendleft(e)

        return completed_count == numCourses