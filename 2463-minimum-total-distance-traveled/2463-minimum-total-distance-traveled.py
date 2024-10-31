class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        
        @cache
        def dp(i,j):
            
            if i >= len(robot):
                return 0
            if j == len(factory):
                return math.inf 
            
            cost = dp(i,j+1)
            another_cost = 0
            for k in range(factory[j][1]):
                if i +k < len(robot):
                    another_cost += abs(robot[i+k] - factory[j][0])
                cost = min(another_cost + dp(i+k+1,j+1), cost)
            return cost
        return dp(0,0)