from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        if len(edges) == 0:
            return True
        # make graph using dictionaries
        # DFS

        nd = defaultdict(list)

        for edge in edges:
            nd[edge[0]].append(edge[1])
            nd[edge[1]].append(edge[0])

        q = deque()
        seen = set()

        q.append(list(nd.keys())[0])

        while q:
            curr = q.popleft()
            if curr in seen:
                return False

            seen.add(curr)
            for j in nd[curr]:
                if j not in seen:
                    q.append(j)
            
        if len(seen) == n:
            return True

        return False
        

