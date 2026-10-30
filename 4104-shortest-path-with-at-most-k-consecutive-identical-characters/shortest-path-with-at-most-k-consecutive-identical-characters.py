class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        g = [[] for _ in range(n)]
        for s, e, w in edges:
            g[s].append((e, w, labels[s] == labels[e]))
        best = [k + 1] * n
        h = [(0, 0, 1)]
        while h:
            d, u, r = heapq.heappop(h)
            if r >= best[u]: continue
            best[u] = r
            if u == n - 1: return d
            for v, w, same in g[u]:
                nr = r + 1 if same else 1
                if nr < best[v]: heapq.heappush(h, (d + w, v, nr))
        return -1