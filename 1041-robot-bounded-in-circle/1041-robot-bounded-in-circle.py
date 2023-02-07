class Solution:
    def isRobotBounded(self, instructions: str) -> bool:

        
        instructions *= 4
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        f = defaultdict(int)
        
        def change(instruction,point):
            
            if instruction == "G":
                f[point] += 1
                
            elif instruction == "L":
                point = (point[1],-point[0])
            else:
                point = (-point[1],point[0])
            
            return point
        
        original_point = (0,1)
        
        for instruction in instructions:
            original_point = change(instruction,original_point)
        
        
        return f[(1,0)] == f[(-1,0)] and f[(0,1)] == f[0,-1]
            