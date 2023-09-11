class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        f = defaultdict(list)
        
        for i in range(len(groupSizes)):
            
            f[groupSizes[i]].append(i)
        
        answer = []
        
        for key in f.keys():
            
            for i in range(0,len(f[key]),key):
                
                possible = f[key][i:i+key]
                
                answer.append(possible)
        
        return answer