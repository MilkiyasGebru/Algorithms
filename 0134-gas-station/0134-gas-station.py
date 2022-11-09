class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1
        
        prefix = []
        for i in range(len(gas)):
            if len(prefix) == 0:
                prefix.append(gas[i]-cost[i])
            else:
                prefix.append(prefix[-1] + gas[i] - cost[i])
        prefix = prefix[::-1]
        last_index =len(cost) - 1 -  prefix.index(min(prefix))
        return (last_index+1)%(len(prefix))