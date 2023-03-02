class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        
        f = defaultdict(int)
        max_diff = 0
        answer = 0
        for i in range(len(nums1)):
            
            max_diff = max(abs(nums1[i] - nums2[i]),max_diff)
            f[abs(nums1[i] - nums2[i])] += 1
        for diff in range(max_diff,0,-1):
            
            sub = min(f[diff],k1)
            f[diff] -= sub
            f[diff - 1] += sub
            k1 -= sub
            
            sub = min(f[diff],k2)
            f[diff] -= sub
            f[diff - 1] += sub
            k2 -= sub
        for key in f.keys():
            
            answer += key*key*f[key]
        
        return answer