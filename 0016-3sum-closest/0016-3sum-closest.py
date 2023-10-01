class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        answer = math.inf
        nums.sort()
        
        for large in range(len(nums)-1,-1,-1):
            small,medium = 0,large-1
            new_target = target - nums[large]
            while small < medium:
                summ = nums[large] + nums[medium] + nums[small]
                if abs(target - answer) > abs(target - summ):
                    answer = summ
                
                if nums[small] + nums[medium] > new_target:
                    medium -= 1
                else:
                    small += 1
        
        return answer
                
                
            