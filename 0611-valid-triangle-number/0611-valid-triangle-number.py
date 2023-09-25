class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        '''
        First Lets sort the sides
        '''
        valid_triangles = 0
        for large in range(len(nums)-1,-1,-1):
            small,medium = 0,large-1
            while small < medium:
                
                if nums[small] + nums[medium] > nums[large] :
                    
                    valid_triangles += medium - small
                    medium -= 1
                else:
                    small += 1
        
        return valid_triangles