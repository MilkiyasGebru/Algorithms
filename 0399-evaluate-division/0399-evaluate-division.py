class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # build adjecency list
        adj_list = {}
        
        for (eq, val) in zip(equations, values):
            if eq[0] not in adj_list:
                adj_list[eq[0]] = []
            adj_list[eq[0]].append((eq[1], val))

            if eq[1] not in adj_list:
                adj_list[eq[1]] = []
            adj_list[eq[1]].append((eq[0], 1 / val))

        n = len(queries)
        ans = [-1] * n

        for i in range(n):
            if queries[i][0] not in adj_list:
                continue
            visited = set()
            que = deque()
            que.append((queries[i][0], 1))

            while que:
                k, v = que.popleft()
                if k == queries[i][1]:
                    ans[i] = v
                    break
                if k in visited:
                    continue
                visited.add(k)
                for b1, b2 in adj_list[k]:
                    que.append((b1, b2 * v))

        return ans