class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:

        @cache
        def dp(bitmask1,index2):
            
            if bitmask1 + 1 == 2**len(nums1):
                return 0
            
            min_sum = math.inf
            
            for i in range(len(nums1)):
                
                if (bitmask1 & (1 << i)) != 0:
                    continue
                    
                bitmask1 ^= (1 << i)
                
                min_sum = min(min_sum, (nums1[i]^nums2[index2])+dp(bitmask1,index2+1))
                
                bitmask1 ^= (1<<i)
            
            return min_sum
        
        return dp(0,0)