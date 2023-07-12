class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        @cache
        def dp(index1,index2,taken):
            
            if index1 == len(nums1) or index2 == len(nums2):
                return 0 if taken else -math.inf
            
            return max(
            nums1[index1]*nums2[index2] + dp(index1+1,index2+1,True),
                dp(index1+1,index2,taken),
                dp(index1,index2+1,taken),
                dp(index1+1,index2+1,taken)
            
            )
        
        return dp(0,0,False)