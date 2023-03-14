class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        
        total_nodes = len(parents)
        self.answer = defaultdict(int)
        
        
        graph = defaultdict(list)
        
        for i in range(1,len(parents)):
            graph[parents[i]].append(i)
        
        
        def rec(root):
            
            nodes = 1
            
            score = 1
            for child in graph[root]:
                
                child_nodes = rec(child)
                score *= child_nodes
                nodes += child_nodes
            
            score *= max(1,len(parents)-nodes)
            self.answer[score] += 1
            
            return nodes
        
        rec(0)
        return max(self.answer.items(), key = lambda x : x[0])[1]
        
        
            
            
            
            
            