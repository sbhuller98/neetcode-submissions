from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)

        for item in prerequisites:
            graph[item[1]].append(item[0])

        seen = set()
        currPath = set()

        def DFS(curr):
            if curr in currPath: return False
            if curr in seen or curr not in graph:
                return True
            
            seen.add(curr)
            currPath.add(curr)

            for item in graph[curr]:
                if not DFS(item):
                    return False

            currPath.remove(curr)
            return True

        for key in graph.keys():
            if not DFS(key):
                return False

        return True