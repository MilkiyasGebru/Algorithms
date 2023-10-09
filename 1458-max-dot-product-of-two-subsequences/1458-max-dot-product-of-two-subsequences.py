class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        @cache
        def dp(i,j,picked):
            
            if i == len(nums1) or j == len(nums2):
                return 0 if picked else -inf
            
            
            return max(
            
                nums1[i]*nums2[j] + dp(i+1,j+1,True),
                dp(i+1,j,picked),
                dp(i,j+1,picked)
            
            )
        
        return dp(0,0,False)