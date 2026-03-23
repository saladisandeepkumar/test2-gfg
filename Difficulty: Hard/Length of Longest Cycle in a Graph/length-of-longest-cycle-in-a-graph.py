class Solution:
    def longestCycle(self, V, edges):
        # code here
        from collections import defaultdict

        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)

        # 0 = unvisited, 1 = entered (on stack), 2 = exited (done)
        state = [0] * V
        depth = [0] * V

        ans = -1

        def dfs(u, d):
            nonlocal ans
            state[u] = 1        # enter node
            depth[u] = d

            for v in g[u]:
                if state[v] == 0:       # unvisited → explore
                    dfs(v, d + 1)
                elif state[v] == 1:     # entered but not exited → cycle
                    cycle_len = depth[u] - depth[v] + 1
                    ans = max(ans, cycle_len)
                # state[v] == 2 → already fully processed, skip

            state[u] = 2        # exit node

        for i in range(V):
            if state[i] == 0:
                dfs(i, 0)

        return ans
        
