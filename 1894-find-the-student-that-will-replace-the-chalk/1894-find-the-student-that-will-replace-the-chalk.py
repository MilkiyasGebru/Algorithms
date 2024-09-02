class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        total_chalks = sum(chalk)
        k = k%total_chalks
        
        for i in range(len(chalk)):
            if chalk[i] > k:
                return i
            k -= chalk[i]
        