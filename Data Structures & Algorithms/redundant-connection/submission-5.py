class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank = [0] * (n+1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a,b):
        parA = self.find(a)
        parB = self.find(b)
        if parA == parB:
            return False
        
        if self.rank[parA] > self.rank[parB]:
            self.parent[parB] = parA
        elif self.rank[parB] > self.rank[parA]:
            self.parent[parA] = parB
        else:
            self.parent[parA] = parB
            self.rank[parB] += 1

        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ans = None
        countNodes = set()

        for edge in edges:
            countNodes.add(edge[0])
            countNodes.add(edge[1])
        
        uf = UnionFind(len(countNodes))

        for edge in edges:
            if not uf.union(edge[0],edge[1]):
                ans = edge

        return ans


        
        
