class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        nums1.sort()
        nums2.sort()
        
        set_one = set(nums1)
        set_two = set(nums2)
        answer =[[],[]]
        
        for i in range(len(nums1)):
            if nums1[i] not in set_two and (len(answer[0]) < 1 or (answer[0][-1] != nums1[i]) ):
                answer[0].append(nums1[i])
        for i in range(len(nums2)):
            if nums2[i] not in set_one and ((len(answer[1]) < 1 or (answer[1][-1] != nums2[i]) )):
                answer[1].append(nums2[i])
        return answer