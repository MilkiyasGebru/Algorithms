class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        waiting_time = 0
        time = customers[0][0]
        for i in range(len(customers)):
            time = max(time,customers[i][0])
            waiting_time += (time + customers[i][1])  - customers[i][0]
            time += customers[i][1]
        return waiting_time/len(customers)