class Solution:
    
    
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        f = defaultdict(list)
        
        for i in range(len(strs)):
            
            f[str(sorted(strs[i]))].append(strs[i])
        
        return f.values()