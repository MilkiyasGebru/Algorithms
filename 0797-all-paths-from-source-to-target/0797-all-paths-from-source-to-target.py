class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        '''
        Topological Sorting is what coming to my mind because its DAG
        '''
        
        all_paths = []
        def dfs(node,path):
            
            if node == len(graph) - 1:
                all_paths.append(path.copy())
                return 
            for neigb in graph[node]:
                dfs(neigb,path+[neigb])
        
        dfs(0,[0])
        
        return all_paths
            

            