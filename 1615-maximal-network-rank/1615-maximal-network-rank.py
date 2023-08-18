class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        networkRank = 0
        graph = defaultdict(set)
        
        for road in roads:
            
            graph[road[0]].add(road[1])
            graph[road[1]].add(road[0])
        
        for city in range(0,n):
            
            for neig in range(city + 1,n):
                
                networkRank = max(networkRank, len(graph[city]) + len(graph[neig]) - 1*(neig in graph[city]))

        
        return networkRank