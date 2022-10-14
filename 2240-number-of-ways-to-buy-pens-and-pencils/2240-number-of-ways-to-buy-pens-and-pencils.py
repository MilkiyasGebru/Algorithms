class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ans = 0
        c = 0
        while(c*cost1 <= total):
            ans += (total-c*cost1)//cost2 + 1
            c+=1
        return ans