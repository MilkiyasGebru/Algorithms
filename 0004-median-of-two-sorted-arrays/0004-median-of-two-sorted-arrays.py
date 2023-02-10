class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums1.extend(nums2)
        nums1.sort()
        index1 = math.floor((len(nums1)-1)/2)
        index2 = math.ceil((len(nums1)-1)/ 2)
        
        return (nums1[index1] + nums1[index2])/2
        