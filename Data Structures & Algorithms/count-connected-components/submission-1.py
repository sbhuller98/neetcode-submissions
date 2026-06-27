from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        components = 0

        seen = set()

        def bfs(nd):
            q = [nd]
            while q:
                curr = q.pop()
                seen.add(curr)
                for connected in graph[curr]:
                    if connected not in seen:
                        q.append(connected)
            


        while True:
            node = None
            for nd in graph.keys():
                if nd not in seen:
                    node = nd
                    break
                
            if node is not None:
                bfs(node)
                components += 1
            else:
                return n - len(seen) + components
            

                
                