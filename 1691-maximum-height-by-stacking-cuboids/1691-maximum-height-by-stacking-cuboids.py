class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        cuboids = [sorted(cuboid) for cuboid in cuboids]
        cuboids.sort(reverse=True)
        max_height = 0
        
        @cache
        def dp(i):
            
            if i == len(cuboids):
                return 0
            max_height = 0
            for j in range(i+1,len(cuboids)):
                
                if cuboids[j][1] <= cuboids[i][1] and cuboids[j][2] <= cuboids[i][2]:
                    max_height = max(max_height, dp(j))
            return max_height + cuboids[i][-1]
        
        for i in range(len(cuboids)):
            max_height = max(max_height, dp(i))
        
        return max_height
                    