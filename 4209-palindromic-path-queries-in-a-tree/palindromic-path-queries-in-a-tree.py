import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(200000)

class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        # 1. Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # 2. Tree flattening / HLD structures
        parent = [0] * n
        depth = [0] * n
        heavy = [-1] * n
        head = [0] * n
        pos = [0] * n
        cur_pos = 0
        
        # First DFS to find subtree sizes, depths, parents, and heavy children
        def dfs1(u, p, d):
            parent[u] = p
            depth[u] = d
            size = 1
            max_sub_size = 0
            for v in adj[u]:
                if v != p:
                    sub_size = dfs1(v, u, d + 1)
                    size += sub_size
                    if sub_size > max_sub_size:
                        max_sub_size = sub_size
                        heavy[u] = v
            return size

        dfs1(0, -1, 0)
        
        # Second DFS to set chain heads and positions in the segment tree
        def dfs2(u, h):
            nonlocal cur_pos
            head[u] = h
            pos[u] = cur_pos
            cur_pos += 1
            
            if heavy[u] != -1:
                dfs2(heavy[u], h)
                
            for v in adj[u]:
                if v != parent[u] and v != heavy[u]:
                    dfs2(v, v)

        dfs2(0, 0)
        
        # 3. Segment Tree Implementation (storing 26-bit XOR bitmasks)
        tree = [0] * (4 * n)
        
        def build(node, start, end):
            if start == end:
                # Find which node corresponds to this segment tree position
                # We can map positions back or initialize with s[u] masks
                return
            # (Alternatively, you can update each node individually after building)
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            
        def update_tree(node, start, end, idx, val):
            if start == end:
                tree[node] = val
                return
            mid = (start + end) // 2
            if start <= idx <= mid:
                update_tree(2 * node, start, mid, idx, val)
            else:
                update_tree(2 * node + 1, mid + 1, end, idx, val)
            tree[node] = tree[2 * node] ^ tree[2 * node + 1]

        def query_tree(node, start, end, l, r):
            if r < start or end < l:
                return 0
            if l <= start and end <= r:
                return tree[node]
            mid = (start + end) // 2
            return query_tree(2 * node, start, mid, l, r) ^ query_tree(2 * node + 1, mid + 1, end, l, r)

        # Initialize segment tree values based on initial string s
        char_masks = [1 << (ord(c) - ord('a')) for c in s]
        for i in range(n):
            update_tree(1, 0, n - 1, pos[i], char_masks[i])
            
        # 4. HLD Path Query function
        def query_path(u, v):
            res = 0
            while head[u] != head[v]:
                if depth[head[u]] > depth[head[v]]:
                    u, v = v, u
                # Query from head[v] to v on the flattened array
                res ^= query_tree(1, 0, n - 1, pos[head[v]], pos[v])
                v = parent[head[v]]
            if depth[u] > depth[v]:
                u, v = v, u
            res ^= query_tree(1, 0, n - 1, pos[u], pos[v])
            return res

        # 5. Process Queries
        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                new_mask = 1 << (ord(c) - ord('a'))
                update_tree(1, 0, n - 1, pos[u], new_mask)
            else:
                u = int(parts[1])
                v = int(parts[2])
                path_mask = query_path(u, v)
                # Check if at most one bit is set: (mask & (mask - 1)) == 0
                if (path_mask & (path_mask - 1)) == 0:
                    ans.append(True)
                else:
                    ans.append(False)
                    
        return ans