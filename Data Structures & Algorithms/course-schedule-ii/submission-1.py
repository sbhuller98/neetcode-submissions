class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        if not prerequisites:
            for i in range(numCourses):
                ans.append(i)
            return ans

        graph = defaultdict(list)
        incomingEdgesCount = defaultdict(int)
        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])
            incomingEdgesCount[prereq[0]] += 1
            incomingEdgesCount[prereq[1]]
        
        q = deque()
        seen = set()
        for key,value in incomingEdgesCount.items():
            if value == 0:
                ans.append(key)
                q.append(key)
                seen.add(key)

        while q:
            curr = q.pop()
            for items in graph[curr]:
                incomingEdgesCount[items] -= 1
                if incomingEdgesCount[items] == 0:
                    q.appendleft(items)
                    ans.append(items)
                    seen.add(items)

        if len(seen) != len(incomingEdgesCount.keys()):
            return []
        
        for i in range(numCourses):
            if i not in seen:
                ans.append(i)

        return ans
