class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        
        
        @cache
        def dp(index,prevSwap):
            
            if index == len(nums1):
                return 0
            
            check1 = (nums1[index] > nums1[index-1]) and (nums2[index] > nums2[index-1])
            check2 = (nums1[index] > nums2[index-1]) and (nums2[index] > nums1[index-1])
            
            not_swap = (prevSwap and check2) or ((not prevSwap) and check1)
            canSwap = (prevSwap and check1) or ((not prevSwap) and check2)
            
            answer = math.inf
            if canSwap:
                answer = min(answer, 1 + dp(index+1,True))
            if not_swap:
                answer = min(answer,dp(index+1,False))
            
            return answer
            
        
        return min(1 + dp(1,True), dp(1,False))