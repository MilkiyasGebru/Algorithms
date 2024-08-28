class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        prev_minn = math.inf
        prev_maxx = -math.inf
        answer = 0
        for array in arrays:
            
            answer = max(array[-1]-prev_minn,prev_maxx - array[0],answer)
            prev_minn = min(array[0],prev_minn)
            prev_maxx = max(array[-1],prev_maxx)
        return answer