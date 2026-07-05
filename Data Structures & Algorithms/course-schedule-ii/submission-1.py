class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        indegree = [0] * numCourses

        for nxt, pre in prerequisites:
            indegree[nxt] += 1
            adj[pre].append(nxt)

        ans = []

        def dfs(n):
            ans.append(n)
            indegree[n] -= 1
            for nei in adj[n]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    dfs(nei)

        for i in range(numCourses):
            if indegree[i] == 0:
                dfs(i)

        return ans if len(ans) == numCourses else []