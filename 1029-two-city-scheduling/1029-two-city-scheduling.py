class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        '''Greedy Approach'''
        
        
        costs.sort(key = lambda x : abs(x[1]-x[0]), reverse=True)
        min_cost,count1,count2 = 0,0,0
        for i in range(len(costs)):
            
            if (count1 < len(costs)//2 and costs[i][0] <= costs[i][1]) or count2 == len(costs)//2:
                count1 += 1
                min_cost += costs[i][0]
            else:
                min_cost += costs[i][1]
                count2 += 1
        
        return min_cost
        
            
            