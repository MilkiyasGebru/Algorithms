class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        '''
        I need to use all the tickets once.... How do I do that???
        
        '''
        
        graph = defaultdict(list)
        for inital,dest in tickets:
            graph[inital].append(dest)
        
        for key in graph.keys():
            graph[key].sort(reverse=True)
        node = "JFK"
        answer = []
        
        def rec(node):
            answer = [node]
            while len(graph[node]):
                node = graph[node].pop()
                answer.append(node)
             
            for i in range(len(answer)-1,-1,-1):
                
                if len(graph[answer[i]]) :
                    array = rec(answer[i])
                    answer = answer[:i] + array + answer[i+1:]
            return answer        
            
            
            
        
        return rec(node)