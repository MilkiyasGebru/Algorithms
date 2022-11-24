class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        children = defaultdict(list)
        for i in range(len(parent)):
            if parent[i] != -1:
                children[parent[i]].append(i)
        self.answer = 1
        def dfs(node):
            
            max1,max2=-inf,-inf
            
            for child in children[node]:
                
                value = dfs(child)*(s[node] != s[child])
                
                if value >= max2:
                    max1 = max2
                    max2 = value
                elif value > max1:
                    max1 = value
            
            self.answer = max(self.answer, 1 + max1 + max2 , 1 + max1, 1 + max2)
            
            return 1 + max(0,max1,max2)
        dfs(0)
        return self.answer
            
            