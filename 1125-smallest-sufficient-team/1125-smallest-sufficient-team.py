class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        f = {}
        person = {}
        total = 2**(len(req_skills)) - 1
        for i in range(len(req_skills)):
            f[req_skills[i]] = 2**i
        
        for i in range(len(people)):
            value = 0
            for skill in people[i]:
                value |= f[skill]
            person[i] = value
        @cache
        def backtrack(i,bitmask):
            
            if i == len(people):

                return (0,[]) if bitmask == total else (math.inf,[])
            
            x1,x2 = backtrack(i+1,bitmask | person[i])
            y1,y2 = backtrack(i+1,bitmask)
            
            if x1 + 1 <= y1:
                
                return (x1+1,x2+[i])
            
            return (y1,y2)
            
        
        return backtrack(0,0)[1]
            