class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        cuts.append(0)
        cuts.append(n)
        cuts.sort()
        
        @lru_cache(None)
        def rec(left_end,right_end):
            
            answer = math.inf
            
            for i in range(left_end+1,right_end):
                answer = min(answer, cuts[right_end]-cuts[left_end] + rec(left_end,i) + rec(i,right_end))
            
            return answer if answer != math.inf else 0
        
        return rec(0,len(cuts)-1)