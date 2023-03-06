class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        arr = set(arr)
        start = 1
        while(True):
            
            if start not in arr:
                k-=1
            if k == 0:
                return start
            start += 1